"""
requires: manim, py3cairo, ffmpeg, pango, pkg-config, scipy, mactex (for mac)
run command: manim -pql scene.py AdditionIntro
"""

from manim import *

class AdditionIntro(Scene):
    def construct(self):
        # Intro
        intro = Text("आइए जोड़ सीखें!", color=BLUE).scale(1.5)
        self.play(Write(intro), run_time=1)
        self.wait(2)
        self.remove(intro)

        # Addition demo using blocks
        blue_blocks = VGroup(*[Square(fill_color=BLUE, side_length=0.9, fill_opacity=1) for _ in range(3)])
        blue_blocks.arrange(RIGHT, buff=0.5)
        blue_blocks.move_to(UP * 2.5)

        orange_blocks = VGroup(*[Square(fill_color=ORANGE, side_length=0.9, fill_opacity=1) for _ in range(2)])
        orange_blocks.arrange(RIGHT, buff=0.5)
        orange_blocks.next_to(blue_blocks, DOWN, buff=1)

        self.play(LaggedStart(*[FadeIn(block) for block in blue_blocks], lag_ratio=0.5), run_time=1)

        blue_counts = []
        for i, block in enumerate(blue_blocks, start=1):
            count = Integer(i)
            count.move_to(block.get_center() + UP * 0.7)
            blue_counts.append(count)
            self.play(block.animate.set_color(YELLOW), run_time=0.3)
            self.play(Write(count), run_time=0.3)
            self.wait(0.2)
            self.play(block.animate.set_color(BLUE), run_time=0.3)

        self.play(LaggedStart(*[FadeIn(block) for block in orange_blocks], lag_ratio=0.5), run_time=1)

        orange_counts = []
        for i, block in enumerate(orange_blocks, start=1):
            count = Integer(i)
            count.move_to(block.get_center() + UP * 0.7)
            orange_counts.append(count)
            self.play(block.animate.set_color(YELLOW), run_time=0.3)
            self.play(Write(count), run_time=0.3)
            self.wait(0.2)
            self.play(block.animate.set_color(ORANGE), run_time=0.3)

        self.play(*[FadeOut(count) for count in blue_counts[:-1]], run_time=1)
        self.play(*[FadeOut(count) for count in orange_counts[:-1]], run_time=1)
        self.play(blue_counts[-1].animate.next_to(blue_blocks, RIGHT, buff=1), run_time=1)
        self.play(orange_counts[-1].animate.next_to(blue_counts[-1], DOWN, buff=1.5), run_time=1)
        self.wait(0.5)

        plus_sign = Text("+", color=GREEN).scale(1.25)
        plus_sign.move_to(blue_counts[-1].get_bottom() + DOWN * 0.75)
        self.play(Create(plus_sign), run_time=0.5)
        self.wait(0.5)
        self.play(plus_sign.animate.move_to(DOWN * 0.5), run_time=0.5)
        self.play(blue_counts[-1].animate.next_to(plus_sign, LEFT, buff=1), run_time=0.5)
        self.play(orange_counts[-1].animate.next_to(plus_sign, RIGHT, buff=1), run_time=0.5)

        second_plus_sign = Text("+", color=GREEN).scale(1.25)
        second_plus_sign.next_to(plus_sign, UP, buff=1)
        second_plus_sign.set_opacity(0)

        self.play(Create(second_plus_sign), run_time=0.5)
        self.play(blue_blocks.animate.next_to(second_plus_sign, LEFT, buff=0.5), run_time=0.5)
        self.play(orange_blocks.animate.next_to(second_plus_sign, RIGHT, buff=0.5), run_time=0.5)
        self.play(second_plus_sign.animate.set_opacity(1), run_time=0.5)

        blue_number_value = int(blue_counts[-1].get_value())
        orange_number_value = int(orange_counts[-1].get_value())
        last_blue_count_mobject = blue_counts[-1]
        last_orange_count_mobject = orange_counts[-1]
        
        all_counts = []
        for block in blue_blocks:
            count = Integer(blue_counts.pop(0).get_value())
            count.move_to(block.get_center() + UP * 0.7)
            all_counts.append(count)
            self.play(block.animate.set_color(YELLOW), run_time=0.3)
            self.play(Write(count), run_time=0.3)
            self.wait(0.2)
            self.play(block.animate.set_color(BLUE), run_time=0.3)

        start_count = all_counts[-1].get_value() + 1  

        for block in orange_blocks:
            count = Integer(start_count)
            count.move_to(block.get_center() + UP * 0.7)
            all_counts.append(count)
            start_count += 1  
            self.play(block.animate.set_color(YELLOW), run_time=0.3)
            self.play(Write(count), run_time=0.3)
            self.wait(0.2)
            self.play(block.animate.set_color(ORANGE), run_time=0.3)

        equal_sign = Text("=", color=GREEN).scale(1.25)
        equal_sign.next_to(orange_blocks, RIGHT, buff=1)
        final_count = Integer(start_count - 1)  
        final_count.next_to(equal_sign, RIGHT, buff=0.5)
        self.play(Create(equal_sign), run_time=0.5)
        self.play(Write(final_count), run_time=0.5)

        numerical_equal_sign = Text("=", color=GREEN).scale(1.25)
        numerical_equal_sign.next_to(plus_sign, RIGHT, buff=2)  
        numerical_total = Integer(blue_number_value + orange_number_value)
        numerical_total.next_to(numerical_equal_sign, RIGHT, buff=0.5)
        self.play(Create(numerical_equal_sign), run_time=0.5)
        self.play(Write(numerical_total), run_time=0.5)

        self.wait(3) 

        self.play(
            *[FadeOut(mob) for mob in all_counts + [equal_sign, final_count, plus_sign, numerical_equal_sign, second_plus_sign, numerical_total, last_blue_count_mobject, last_orange_count_mobject] + list(blue_blocks) + list(orange_blocks)]
        )

        # Display a simple sum formula
        sum_formula = MathTex("3", "+", "2", "=", "5")
        sum_formula.scale(2)
        sum_formula.move_to(ORIGIN)
        self.play(Write(sum_formula))
        self.wait()

        explanations_positions = {
            "3": {"direction": DOWN, "buff": 2},
            "+": {"direction": UP, "buff": 2},
            "2": {"direction": DOWN, "buff": 1},
            "=": {"direction": UP, "buff": 1.5},
            "5": {"direction": DOWN, "buff": 2},
        }

        # Hindi explanations for each part of the equation
        explanations = [
            ("3", "तीन (जोड़ने की पहली संख्या)"),
            ("+", "'प्लस' या 'जोड़' का चिन्ह"),
            ("2", "दो (जोड़ने की दूसरी संख्या)"),
            ("=", "'बराबर' का चिन्ह"),
            ("5", "पांच (जोड़ का परिणाम)")
        ]

        for tex, explanation in explanations:
            position_info = explanations_positions[tex]
            target = sum_formula.get_part_by_tex(tex)
            
            explanation_text = Text(explanation, font_size=24, color=BLUE)
            explanation_text.next_to(target, position_info["direction"], buff=position_info["buff"])
            
            if tex == "3":
                explanation_text.shift(LEFT * 0.5) 
            elif tex == "5":
                explanation_text.shift(RIGHT * 0.5) 
            
  
            arrow_start = explanation_text.get_top() if np.all(position_info["direction"] == DOWN) else explanation_text.get_bottom()
            arrow_end = target.get_bottom() if np.all(position_info["direction"] == DOWN) else target.get_top()

            arrow = Arrow(arrow_start, arrow_end, buff=0.1, color=RED)

            self.play(Write(explanation_text), GrowArrow(arrow))
            self.wait(1)

        self.wait(2)
