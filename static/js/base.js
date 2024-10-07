    const button = document.querySelector('button');

        button.addEventListener('mouseenter', () => {
            button.style.transform = 'rotate(5deg)';
        });

        button.addEventListener('mouseleave', () => {
            button.style.transform = 'rotate(0deg)';
        });