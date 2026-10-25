'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { resolve, search } = require('./navigation-core.js');
const root = path.resolve(__dirname, '..');
const read = relative => JSON.parse(fs.readFileSync(path.join(root, relative), 'utf8'));
const navigation = read('catalog/navigation.json');
const fixtures = read('catalog/navigation-cases.json').cases;
const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
const data = JSON.parse(html.match(/<script id="atlas-data" type="application\/json">([\s\S]*?)<\/script>/)[1]);
assert.deepEqual(data.navigation, navigation);
assert.deepEqual(data.vocabulary, read('catalog/search-terms.json'));
assert.ok(html.includes(fs.readFileSync(path.join(root, 'tools/navigation-core.js'), 'utf8')));
const catalog = read('catalog/skills.json');
for (const entry of catalog.skills) {
  const skill = data.skills[entry.id];
  assert.equal(skill.status, entry.facts.status);
  assert.equal(skill.collection, entry.facts.collection);
  assert.deepEqual(skill.interpretation, entry.interpretation);
}
assert.equal(new Set(navigation.goals.map(item => item.id)).size, navigation.goals.length);
const nodes = navigation.questions, outcomes = navigation.outcomes, seen = new Set();
assert.ok(!Object.keys(nodes).some(id => outcomes[id]));
function visit(id, active = new Set()) {
  assert.ok(!active.has(id), 'Cycle: ' + id);
  assert.ok(nodes[id] || outcomes[id], 'Missing target: ' + id);
  if (seen.has(id)) return;
  seen.add(id);
  if (!nodes[id]) return;
  const question = nodes[id];
  assert.ok(question.question && question.hint);
  assert.ok(question.choices.length >= 2 && question.choices.length <= 5);
  assert.equal(new Set(question.choices.map(item => item.id)).size, question.choices.length);
  for (const choice of question.choices) visit(choice.next, new Set([...active, id]));
}
for (const goal of navigation.goals) visit(goal.start);
assert.equal(seen.size, Object.keys(nodes).length + Object.keys(outcomes).length);
for (const result of Object.values(outcomes)) {
  for (const field of ['title','why','next_step','boundary']) assert.ok(result[field]);
  assert.ok(result.prerequisites.length);
  for (const id of [result.primary, result.alternative?.id, ...result.support.map(item => item.id)].filter(Boolean)) {
    assert.ok(data.skills[id], 'Unknown skill: ' + id);
    assert.equal(data.skills[id].status, 'stable', 'Unpromoted default: ' + id);
  }
  if (result.alternative) assert.ok(result.alternative.when);
  for (const support of result.support) assert.ok(support.when);
  if (result.playbook) assert.equal(result.primary, 'poteto/poteto-mode');
}
const covered = new Set();
for (const fixture of fixtures) {
  const result = resolve(navigation, fixture.goal, fixture.answers);
  assert.equal(result.state, 'result', fixture.scenario);
  assert.equal(result.id, fixture.expected_outcome, fixture.scenario);
  assert.equal(result.value.primary, fixture.expected_primary, fixture.scenario);
  assert.ok(result.trail.length <= 3, 'Too many follow-ups');
  covered.add(result.id);
}
assert.equal(covered.size, Object.keys(outcomes).length);
assert.equal(resolve(navigation, null).state, 'goal');
assert.equal(resolve(navigation, 'test').id, 'test-intent');
assert.equal(resolve(navigation, 'test', {'test-intent':'strategy'}).id, 'module-execution');
assert.throws(() => resolve(navigation, 'test', {'test-intent':'invented-answer'}), /Unknown answer/);
const isolated = resolve(navigation, 'test', {'test-intent':'strategy','module-execution':'isolated'});
const analysis = resolve(navigation, 'test', {'test-intent':'strategy','module-execution':'analysis'});
assert.equal(isolated.value.primary, 'matt/codebase-design');
assert.equal(analysis.value.primary, 'matt/codebase-design');
assert.match(isolated.value.boundary, /not.*coordinator/i);
assert.match(analysis.value.boundary, /do not run code/i);
assert.match(isolated.value.alternative.when, /agree.*seams/i);
assert.match(analysis.value.alternative.when, /allow execution/i);
assert.notEqual(isolated.id, analysis.id);
const keywordCases = [
  ['analyze how to test a module in a system without running the system', 'matt/codebase-design'],
  ['testar modulo isolado sem rodar sistema', 'matt/codebase-design'],
  ['write specification before coding', 'matt/to-spec'],
  ['triage incoming reports', 'matt/triage'],
  ['parallel coverage workers', 'poteto/swarm'],
  ['improve prompt', 'poteto/sharpen'],
  ['matt/tdd', 'matt/tdd']
];
for (const [query, expected] of keywordCases) {
  const matches = search(data.skills, query, {}, data.vocabulary);
  assert.equal(matches[0]?.skill.id, expected, query);
}
assert.equal(search(data.skills, 'zxqv-no-such-capability', {}, data.vocabulary).length, 0);
assert.equal(search(data.skills, 'the and of', {}, data.vocabulary).length, 0);
assert.ok(search(data.skills, 'tdd', {collection:'poteto'}, data.vocabulary).every(item => item.skill.collection === 'poteto'));
const defaults = search(data.skills, '', {}, data.vocabulary);
assert.ok(defaults.every(item => item.skill.status === 'stable' && item.skill.interpretation.kind !== 'principle'));
const all = search(data.skills, '', {includeUnpromoted:true,includePrinciples:true}, data.vocabulary);
assert.equal(all.length, catalog.skills.length);
for (const id of Object.keys(data.vocabulary.aliases)) assert.ok(data.skills[id], 'Unknown vocabulary target: ' + id);
const report = {status:'pass',goals:navigation.goals.length,questions:Object.keys(nodes).length,outcomes:Object.keys(outcomes).length,guided_scenarios:fixtures.length,search_scenarios:keywordCases.length,all_skills_browsable:all.length,user_module_case:{isolated:isolated.id,analysis_only:analysis.id,primary:isolated.value.primary},missing_answers_preserved:true,unknown_answers_rejected:true,lifecycle_and_collection_filters:true,scope:'Regression checks of source-backed selection rules; improved real-user success is not measured.'};
fs.writeFileSync(path.join(root,'catalog/navigation-validation.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report));
