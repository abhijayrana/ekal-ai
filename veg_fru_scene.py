from manim import *

class FruitsAndVegetablesLesson(Scene):
    def construct(self):
        self.teach_vegetables()
        self.teach_fruits()
        self.show_end_screen()
        

    def teach_vegetables(self):
        # Display the vegetables
        vegetables = ImageMobject("assets/vegetables.jpeg").set_width(4)
        vegetables_label = Text("सब्जियाँ", font="Arial").scale(0.8).next_to(vegetables, DOWN)
        self.play(FadeIn(vegetables), Write(vegetables_label))
        self.wait(8)
        self.play(FadeOut(vegetables), FadeOut(vegetables_label))

        # Highlight individual vegetables one by one
        vegetables_data = [
            {"image": "assets/tomato.jpeg", "label": "टमाटर"},
            {"image": "assets/onion.jpeg", "label": "प्याज"},
            {"image": "assets/eggplant.jpeg", "label": "बैंगन"}
        ]

        for vegetable_data in vegetables_data:
            vegetable = ImageMobject(vegetable_data["image"]).set_width(3)
            vegetable_label = Text(vegetable_data["label"], font="Arial").scale(0.6).next_to(vegetable, DOWN)
            self.play(FadeIn(vegetable), Write(vegetable_label))
            self.play(Indicate(vegetable_label))
            self.wait(5)
            self.play(FadeOut(vegetable), FadeOut(vegetable_label))

    def teach_fruits(self):
        # Display the fruits
        fruits = ImageMobject("assets/fruits.jpeg").set_width(4)
        fruits_label = Text("फल", font="Arial").scale(0.8).next_to(fruits, DOWN)
        self.play(FadeIn(fruits), Write(fruits_label))
        self.wait(8)
        self.play(FadeOut(fruits), FadeOut(fruits_label))

        # Highlight individual fruits one by one
        fruits_data = [
            {"image": "assets/watermelon.jpeg", "label": "तरबूज"},
            {"image": "assets/oranges.jpeg", "label": "संतरे"},
            {"image": "assets/apples.jpeg", "label": "सेब"},
            {"image": "assets/banana.jpeg", "label": "केला"}
        ]

        for fruit_data in fruits_data:
            fruit = ImageMobject(fruit_data["image"]).set_width(3)
            fruit_label = Text(fruit_data["label"], font="Arial").scale(0.6).next_to(fruit, DOWN)
            self.play(FadeIn(fruit), Write(fruit_label))
            self.play(Indicate(fruit_label))
            self.wait(5)
            self.play(FadeOut(fruit), FadeOut(fruit_label))
            
    def show_end_screen(self):
        # Display both fruits and vegetables pictures on the bottom half
        vegetables = ImageMobject("assets/vegetables.jpeg").set_width(4).shift(DOWN * 1.5 + LEFT * 3)
        fruits = ImageMobject("assets/fruits.jpeg").set_width(4).shift(DOWN * 1.5 + RIGHT * 3)

        self.play(FadeIn(vegetables), FadeIn(fruits))
        self.wait(3)

        # Display "धन्यवाद" message on the top half
        thanks_text = Text("धन्यवाद", font="Arial", color=YELLOW).scale(1.5).shift(UP * 1.5)
        self.play(Write(thanks_text))
        self.wait(2)

        self.play(FadeOut(vegetables), FadeOut(fruits), FadeOut(thanks_text))