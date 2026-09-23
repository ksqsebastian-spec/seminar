import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {toolkit} from '../public/toolkit.js';
const c=JSON.parse(await fs.readFile('public/curriculum.json','utf8'));
test('ten sequential lessons teach and verify work in participants own accounts',async()=>{
 assert.equal(c.lessons.length,10);assert.equal(new Set(c.lessons.map(l=>l.id)).size,10);
 for(const l of c.lessons){assert.ok(l.mission&&l.outcome&&l.carry);assert.ok(l.demos.length>=2);assert.ok(l.skills.length>=4);assert.ok(l.checks.length>=3);assert.equal(Object.values(l.rhythm).reduce((a,b)=>a+b,0),l.minutes);assert.ok(l.question.options[l.question.correct]);for(const f of l.files)await fs.access('public/material/'+f);for(const d of l.demos)if(d.asset)await fs.access('public/screens/'+d.asset);}
});
test('two teaching days each fit 09:00 to 16:00 including breaks',()=>{
 for(const d of c.schedule){let expected=9*60;for(const [time,,duration] of d.items){const [h,m]=time.split(':').map(Number);assert.equal(h*60+m,expected);expected+=parseInt(duration,10)}assert.equal(expected,16*60);}
});
test('reference handbook has usable guidance, prompts and verification',()=>{
 assert.equal(toolkit.length,5);for(const t of toolkit){assert.ok(t.items.length>=6);for(const f of t.items)assert.ok(f.slice(0,4).every(Boolean));}
});
