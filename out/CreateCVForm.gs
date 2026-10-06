/**
 * Builds the "CV & Covering Letter Questionnaire" Google Form.
 * How to use:
 *  1. Go to https://script.google.com -> New project
 *  2. Delete the sample code, paste this whole file, click Save
 *  3. Click Run (choose createCVForm), approve the permissions
 *  4. Open View > Logs (or Executions): the form's edit link and share link are printed
 * Question types: 'S' = short answer, 'P' = paragraph, 'Y' = Yes/No/Other choice.
 */
var SECTIONS = [
 ['Section A – The job you are applying for', [
  ['S','Job title and company name (example: Guest Experience Assistant, Hilton London)',true],
  ['S','Location of the job',true],
  ['P','Paste the FULL job advert text (responsibilities, required skills, desirable skills, closing date). If you have no advert yet, write NO ADVERT and answer the next question.',true],
  ['P','If no advert: which sector (hospitality / events / aviation / tourism) and what type of role do you prefer?',false],
  ['S','Name and title of the person the letter is addressed to (or write Hiring Manager)',true],
  ['P','What do you know about this company and why do you want to work there? (2–3 sentences: values, awards, news, reputation)',true]]],
 ['Section B – Contact details', [
  ['S','Full name (as it should appear on the CV)',true],
  ['S','Phone number (with country code if outside the UK)',true],
  ['S','Email address (professional-looking)',true],
  ['S','City / area (full street address is not needed)',true],
  ['S','LinkedIn URL or online portfolio (optional)',false],
  ['Y','Do you have the right to work in the UK?',true]]],
 ['Section C – Education & qualifications', [
  ['S','Current course title and level (e.g. BA International Tourism Management)',true],
  ['S','University name and city',true],
  ['S','Start date and expected graduation date',true],
  ['S','Current grades or predicted classification (optional, e.g. 2:1 average, 68%)',false],
  ['P','Relevant modules you have studied, with grades if you want (e.g. Marketing for Tourism, Events Management, this module)',false],
  ['P','Group projects, case studies, dissertation, field trips or placement: what was it and what was YOUR role?',false],
  ['P','School or college qualifications: subject, level, grade, year (A-levels, BTEC, IB, GCSEs or equivalent)',true],
  ['P','Certificates or training (first aid, food hygiene, safeguarding, IELTS, software courses, etc.)',false]]],
 ['Section D – Work experience (include part-time jobs, internships, volunteering, family business; most recent first)', [
  ['S','JOB 1: Job title, employer, location, start–end dates',true],
  ['P','JOB 1: What did you do day to day? (4–6 points: customers served, tasks, systems used, who you worked with)',true],
  ['P','JOB 1: Best achievement(s), with numbers if possible (e.g. handled 100+ customers per shift, trained 3 new staff, raised £500)',true],
  ['S','JOB 2: Job title, employer, location, start–end dates',false],
  ['P','JOB 2: What did you do day to day? (4–6 points)',false],
  ['P','JOB 2: Best achievement(s), with numbers if possible',false],
  ['S','JOB 3: Job title, employer, location, start–end dates',false],
  ['P','JOB 3: What did you do day to day? (4–6 points)',false],
  ['P','JOB 3: Best achievement(s), with numbers if possible',false]]],
 ['Section E – Skills', [
  ['S','Languages you speak and your level (e.g. English fluent, Hindi native, French basic)',true],
  ['P','IT skills (Word, Excel, PowerPoint, Canva, social media, booking or POS systems, Amadeus/Opera, etc.)',true],
  ['P','Teamwork: give one real example (where, what you did, what happened)',true],
  ['P','Communication / customer service: give one real example',true],
  ['P','Leadership or responsibility: give one real example',false],
  ['P','Problem-solving or working under pressure: give one real example',false],
  ['P','Any other skills (cash handling, photography, driving licence, first aid, cooking, etc.)',false]]],
 ['Section F – Interests & achievements', [
  ['P','Hobbies and interests',true],
  ['P','Sports, clubs or university societies (and any role you held)',false],
  ['P','Volunteering or charity work',false],
  ['P','Travel experience (countries visited, cultural exposure)',false],
  ['P','Awards, scholarships, prizes or competitions',false],
  ['P','Any other achievement you are proud of',false]]],
 ['Section G – Personal profile & career goals', [
  ['P','Describe your career goal in one sentence',true],
  ['P','Why do you want to work in this sector?',true],
  ['P','What makes you different from other applicants? (3 strengths)',true],
  ['P','Which of your experiences best match the job advert?',true],
  ['P','What are you hoping to learn or achieve in this role?',false]]],
 ['Section H – References and final choices', [
  ['P','Referee 1: name, job title, organisation, email/phone (an academic tutor is a good choice) – or write References available on request',false],
  ['P','Referee 2: name, job title, organisation, email/phone (e.g. a manager)',false],
  ['Y','Do you want a photo on the CV? (UK CVs normally do not include one; recommended: No)',true],
  ['S','Preferred output format (Word .docx, PDF, or both)',true],
  ['P','Anything else I should know?',false]]]
];

function createCVForm() {
  var form = FormApp.create('CV & Covering Letter Questionnaire – MGT2001');
  form.setDescription('MGT2001 Enterprise and Consultancy for Tourism – Assessment 1 (CV max 2 A4 pages, Cover Letter 1 A4 page). Answer with short notes or bullet points. Write N/A if something does not apply. Only give real information.');
  form.setProgressBar(true);
  SECTIONS.forEach(function (sec, i) {
    if (i > 0) form.addPageBreakItem().setTitle(sec[0]); else form.addSectionHeaderItem().setTitle(sec[0]);
    sec[1].forEach(function (q) {
      var item;
      if (q[0] === 'S') item = form.addTextItem();
      else if (q[0] === 'P') item = form.addParagraphTextItem();
      else item = form.addMultipleChoiceItem().setChoiceValues(['Yes','No']).showOtherOption(true);
      item.setTitle(q[1]).setRequired(q[2]);
    });
  });
  Logger.log('Edit link: ' + form.getEditUrl());
  Logger.log('Share link: ' + form.getPublishedUrl());
}
