const questions = document.querySelectorAll('.question');

questions.forEach(question => {
    const answer = question.querySelector('.answer');
    question.addEventListener('click', () => {
        answer.style.display = answer.style.display === 'none' ? 'block' : 'none';
    });
});
