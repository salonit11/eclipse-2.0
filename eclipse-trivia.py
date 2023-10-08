import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)


# Trivia Questions and Answers
questions = [
    {
        "question": "How do eclipses occur?",
        "options": [
            "A. When one celestial body moves into the shadow of another celestial body.",
            "B. During the equinox.",
            "C. Randomly, without any pattern."
        ],
        "correct_answer": "A"
    },
    {
        "question": "Why do only some people on Earth see an \neclipse at a given time?",
        "options": [
            "A. Eclipses are visible only from specific regions\n on Earth where the alignment of the Sun, Moon, and Earth is accurate.",
            "B. Eclipses are visible from everywhere on Earth simultaneously.",
            "C. Eclipses are only visible from space stations."
        ],
        "correct_answer": "A"
    },
    {
        "question": "What causes the Sun, Moon, and Earth to align?",
        "options": [
            "A. Gravitational forces.",
            "B. The orbits of the Earth and Moon occasionally align in a straight line.",
            "C. Magnetic forces."
        ],
        "correct_answer": "B"
    },
    {
        "question": "How often do eclipses occur?",
        "options": [
            "A. Daily.",
            "B. Several times a year, but may not be visible from all locations.",
            "C. Once in a century."
        ],
        "correct_answer": "B"
    },
    {
        "question": "How do scientists predict eclipses?",
        "options": [
            "A. Using weather forecasts.",
            "B. Using astronomical calculations to determine the \nexact time and location of eclipses.",
            "C. By observing animal behavior."
        ],
        "correct_answer": "B"
    },
    {
        "question": "What is the difference between a lunar and solar eclipse?",
        "options": [
            "A. A lunar eclipse occurs when the Earth passes between the Sun and the Moon, while\n a solar eclipse occurs when the Moon passes between the Sun and the Earth.",
            "B. A lunar eclipse occurs when the Moon passes between the Sun and the Earth, while\n a solar eclipse occurs when the Earth passes between the Sun and the Moon.",
            "C. There is no difference."
        ],
        "correct_answer": "A"
    },
    {
        "question": "What is an eclipse season?",
        "options": [
            "A. A period when eclipses are impossible.",
            "B. A period when the Sun is close to the lunar nodes, \nincreasing the likelihood of eclipses.",
            "C. A period of intense heat during summer."
        ],
        "correct_answer": "B"
    },
    {
        "question": "During a solar eclipse, what is the phenomenon \ncalled when a ring of sunlight is visible around the moon?",
        "options": [
            "A. Solar Halo",
            "B. Solar Flare",
            "C. Diamond Ring Effect"
        ],
        "correct_answer": "C"
    },
    {
        "question": "What is the term for a partial lunar eclipse where\n only a part of the moon enters Earth's umbral shadow?",
        "options": [
            "A. Penumbra",
            "B. Penumbral Eclipse",
            "C. Totality"
        ],
        "correct_answer": "B"
    },
    {
        "question": "Which ancient civilization believed that a dragon \nor a demon was swallowing the sun during a solar eclipse?",
        "options": [
            "A. Greek",
            "B. Egyptian",
            "C. Chinese"
        ],
        "correct_answer": "C"
    },
    {
        "question":"Why don't we have an eclipse every month?",
        "options": [
            "A. Because eclipses are rare events.",
            "B. Because the Moon's orbit is tilted relative to Earth's \norbit around the Sun.",
            "C. Because the Sun is too bright for eclipses to occur frequently."
        ],
        "correct_answer":"B"
    },
    {
       "question":" What is the umbra during a lunar eclipse?",
       "options": [
            "A. The outer part of the Earth's shadow.",
            "B. The inner, darkest part of the Earth's shadow where the \nMoon is completely blocked from the Sun's light.",
            "C. A type of lunar rock."
       ],
        "correct_answer": "B"
    },
    {
       "question": "During a solar eclipse, what is the bright ring of \nsunlight that surrounds the Moon called?",
         "options": [
             "A. Corona.",
            "B. Umbra.",
            "C. Diamond ring effect."
         ],
        "correct_answer": "C"
    }
    # Add more questions similarly
]

current_question_index = 0
score = 0

# Pygame Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eclipse Trivia Game")
clock = pygame.time.Clock()

# Load Background Image
background_image = pygame.image.load("eclipse.jpeg").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Custom Fonts
question_font = pygame.font.Font("Fendysa.ttf", 30)  # Replace "font.ttf" with your font file path
option_font = pygame.font.Font("Milchella-Regular.ttf", 20)  # Replace "font.ttf" with your font file path

# Game Loop
running = True
while running and current_question_index < 13:
    screen.blit(background_image, (0, 0))

    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the user clicked on an answer option
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i, option_rect in enumerate(option_rects):
                if option_rect.collidepoint(mouse_x, mouse_y):
                    selected_option = chr(ord('A') + i)
                    if selected_option == questions[current_question_index]["correct_answer"]:
                        score += 1
                    current_question_index += 1
    
    if current_question_index < len(questions):
        question_lines = questions[current_question_index]["question"].split('\n')
        for i, line in enumerate(question_lines):
            question_text = question_font.render(line, True, YELLOW)
            screen.blit(question_text, (WIDTH//2 - question_text.get_width()//2, 100 + i * 50))

        # Draw Options with Line Breaks
        option_rects = []
        options = questions[current_question_index]["options"]
        for i, option in enumerate(options):
            option_lines = option.split('\n')
            for j, line in enumerate(option_lines):
                option_text = option_font.render(line, True, YELLOW)
                option_rect = option_text.get_rect(center=(WIDTH//2, 250 + i * 80 + j * 30))
                option_rects.append(option_rect)
                screen.blit(option_text, option_rect.topleft)

        
        # Draw Score
        score_font = pygame.font.Font(None, 36)
        score_text = score_font.render(f"Score: {score}", True, YELLOW)
        screen.blit(score_text, (WIDTH-200, 50))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()