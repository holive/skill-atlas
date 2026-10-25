(function (root) {
  'use strict';

  function resolve(navigation, goalId, answers = {}) {
    const goal = navigation.goals.find(item => item.id === goalId);
    if (!goal) return { state: 'goal', trail: [] };
    let id = goal.start;
    const trail = [];
    const seen = new Set();
    while (navigation.questions[id]) {
      if (seen.has(id)) throw new Error('Navigation cycle');
      seen.add(id);
      const question = navigation.questions[id];
      const answer = answers[id];
      if (answer === undefined) return { state: 'question', id, value: question, trail };
      const choice = question.choices.find(item => item.id === answer);
      if (!choice) throw new Error('Unknown answer for ' + id);
      trail.push({ questionId: id, question: question.question, answer, label: choice.label });
      id = choice.next;
    }
    if (!navigation.outcomes[id]) throw new Error('Unknown outcome ' + id);
    return { state: 'result', id, value: navigation.outcomes[id], trail };
  }

  function normalize(value) {
    return value.toLowerCase().normalize('NFKD').replace(/[\u0300-\u036f]/g, '');
  }

  function search(skills, query, options = {}, vocabulary = {}) {
    const canonical = new Map();
    for (const [term, variants] of Object.entries(vocabulary.synonyms || {})) {
      for (const variant of [term, ...variants]) canonical.set(normalize(variant), term);
    }
    const stop = new Set(vocabulary.stopwords || []);
    function tokens(text) {
      return [...new Set((normalize(text).match(/[\p{L}\p{N}]+/gu) || [])
        .filter(word => !stop.has(word))
        .map(word => canonical.get(word) || word))];
    }
    const terms = tokens(query);
    const rawQuery = normalize(query).trim();
    const entries = [];
    for (const skill of Object.values(skills)) {
      if (options.collection && skill.collection !== options.collection) continue;
      if (!options.includeUnpromoted && skill.status !== 'stable') continue;
      if (!options.includePrinciples && skill.interpretation.kind === 'principle') continue;
      const info = skill.interpretation;
      const fields = [
        [12, skill.id], [8, (vocabulary.aliases || {})[skill.id] || ''],
        [4, info.when_to_use.join(' ')], [3, info.summary],
        [3, info.outputs.join(' ')], [2, info.intents.join(' ')]
      ].map(([weight, text]) => [weight, new Set(tokens(text))]);
      const matched = terms.filter(term => fields.some(([, words]) => words.has(term)));
      const exactId = rawQuery && normalize(skill.id).includes(rawQuery);
      if (terms.length && matched.length < Math.min(2, terms.length) && !exactId) continue;
      if (rawQuery && !terms.length) continue;
      const score = matched.reduce((sum, term) => sum + Math.max(0, ...fields.filter(([, words]) => words.has(term)).map(([weight]) => weight)), 0) + (exactId ? 40 : 0);
      entries.push({ skill, score, matched });
    }
    return entries.sort((a, b) => b.matched.length - a.matched.length || b.score - a.score || a.skill.id.localeCompare(b.skill.id));
  }

  const api = { resolve, search, normalize };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.SkillAtlas = api;
})(typeof globalThis === 'undefined' ? this : globalThis);
