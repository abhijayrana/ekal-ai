from manim import *

class CountingScene(Scene):
    def construct(self):
        intro = Text("ஆங்கிலத்தில் 0 முதல் 10 வரை கற்போம்!", font="Arial")
        self.play(Write(intro))
        self.wait(2)
        self.play(FadeOut(intro))

        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        for number in numbers:
            self.introduceNumber(number)

        outro = Text("நன்றி!", font="Arial")
        self.play(Write(outro))
        self.wait(3)
        self.play(FadeOut(outro))

    def introduceNumber(self, number):
        numbers = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

        numberInt = Integer(number=number).scale(1.5)
        numberInt.move_to(LEFT * 1)

        numberToRender = Text(numbers[number], font="Arial").scale(1).next_to(numberInt, RIGHT, buff=0.5)

        self.play(Write(numberInt))
        self.wait(1)

        for x in range(0, len(numbers[number])):
            self.play(Write(numberToRender[x]))
            self.play(Indicate(numberToRender[x]), run_time=0.2)
            self.wait(0.2)

        blocks = VGroup(*[Square(fill_color=BLUE, side_length=0.5, fill_opacity=1) for _ in range(number)])
        blocks.arrange(RIGHT, buff=0.5)
        blocks.move_to(DOWN * 2)

        self.play(LaggedStart(*[FadeIn(block) for block in blocks], lag_ratio=0.5), run_time=2)
        self.wait(0.2)

        for i, block in enumerate(blocks, start=1):
            count = Integer(i)
            count.move_to(block.get_center() + DOWN * 0.7)
            self.play(block.animate.set_color(YELLOW), run_time=0.3)
            self.wait(0.3)
            self.play(block.animate.set_color(BLUE), run_time=0.3)
            self.wait(0.2)

        self.play(FadeOut(numberInt), FadeOut(numberToRender), FadeOut(blocks))
