#!/user/bin/env python

from big_ol_pile_of_manim_imports import *
import numpy as np

class Function(Scene):

    def construct(self):
        
        Function_open = TextMobject("Function?").set_color(PURPLE)
        Function_open.scale(4)

        cover_text = TextMobject("We Have Covered...")
        cover_text.scale(1)

        topics_array = TextMobject("For Loops", "While Loops", "If/Else Statements")
        topics_array.scale(1)
        topics_array[0].set_color(GREEN)
        topics_array[1].set_color(BLUE)
        topics_array[2].set_color(YELLOW)

        function_text = TextMobject("Function:").set_color(PURPLE)
        function_text.scale(1.5)

        square = Square()
        square.scale(3)

        sq_text = TextMobject("A Function Is Like a Box")
        sq_text2 = TextMobject("Which Can Contain Any Or All Of These Models")
        sq_text.scale(0.8)
        sq_text2.scale(0.65)

        function_code = TextMobject("define","function", "(parameters):")
        function_code[0].set_color(BLUE)
        function_code[1].set_color(YELLOW)

        code = TextMobject("def", "function", "(x):")
        code[0].set_color(BLUE)
        code[1].set_color(YELLOW)

        define_mean = TextMobject("Is The Act Of Defining Your Function")
        function_mean = TextMobject("Is The Name Of Such Function")
        par_mean = TextMobject("Is The Parameters You Desire To Pass Through")
        define_mean.scale(0.75)
        function_mean.scale(0.75)
        par_mean.scale(0.75)

        self.play(Write(Function_open), run_time=3)
        self.wait(2)
        self.play(FadeOutAndShiftDown(Function_open))
        self.wait(1)
        self.play(Write(cover_text), run_time=2)
        self.wait(1)
        self.play(cover_text.shift, 2*UP)
        self.wait(1)
        self.play(FadeIn(topics_array[0]))
        self.wait(1)
        self.play(topics_array[0].shift, 0.5*UP)
        self.wait(1)
        self.play(FadeIn(topics_array[1]))
        self.wait(1)
        self.play(topics_array[1].shift, 0.5*UP)
        self.wait(1)
        self.play(FadeIn(topics_array[2]))
        self.wait(1)
        self.play(topics_array[2].shift, 0.5*UP)
        self.wait(1)
        self.play(topics_array.shift, 0.5*RIGHT)
        self.wait(3)
        self.play(ReplacementTransform(cover_text, function_text))
        self.play(function_text.shift, 2*UP)
        self.play(function_text.shift, 3*LEFT)
        self.wait(2)
        self.play(topics_array[0].shift, 0.5*RIGHT)
        self.play(topics_array[1].shift, 2*LEFT)
        self.play(topics_array[1].shift, 0.75*DOWN)
        self.play(topics_array[2].shift, 5*LEFT)
        self.play(topics_array[2].shift, 1.5*DOWN)
        self.wait(3)
        self.play(FadeInFrom(square), direction=DOWN)
        self.play(square.shift, 2*LEFT)
        self.wait(2)
        self.play(square.shift, 1.5*LEFT)
        self.wait(1)
        self.play(function_text.shift, 1.3*LEFT)
        self.play(topics_array.shift, 1.2*LEFT)
        self.wait(2)
        self.play(Write(sq_text), run_time=2)
        self.play(sq_text.shift, 2.5*RIGHT)
        self.play(sq_text.shift, 1.5*UP)
        self.wait(1)
        self.play(Write(sq_text2), run_time=2)
        self.play(sq_text2.shift, 3.25*RIGHT)
        self.play(sq_text2.shift, 0.5*UP)
        self.wait(3)
        self.play(FadeOut(topics_array))
        self.play(FadeOut(sq_text), FadeOut(sq_text2), FadeOut(function_text))
        self.wait(2)
        self.play(ReplacementTransform(square, function_code))
        self.wait(2)
        self.play(function_code[0].shift, 1*UP)
        self.play(function_code[0].shift, 1*LEFT)
        self.wait(1)
        self.play(Write(define_mean), run_time=3)
        self.play(define_mean.shift, 1*UP)
        self.play(define_mean.shift, 0.5*RIGHT)
        self.wait(2)
        self.play(function_code[0].shift, 1*DOWN)
        self.play(function_code[0].shift, 1*RIGHT)
        self.wait(1)
        self.play(function_code[1].shift, 1*UP)
        self.play(function_code[1].shift, 2.5*LEFT)
        self.wait(1)
        self.play(ReplacementTransform(define_mean, function_mean))
        self.play(function_mean.shift, 1*UP)
        self.play(function_mean.shift, 0.5*RIGHT)
        self.wait(2)
        self.play(function_code[1].shift, 1*DOWN)
        self.play(function_code[1].shift, 2.5*RIGHT)
        self.wait(1)
        self.play(function_code[2].shift, 1*UP)
        self.play(function_code[2].shift, 6*LEFT)
        self.wait(1)
        self.play(ReplacementTransform(function_mean, par_mean))
        self.play(par_mean.shift, 1*UP)
        self.play(par_mean.shift, 1.5*RIGHT)
        self.wait(2)
        self.play(function_code[2].shift, 1*DOWN)
        self.play(function_code[2].shift, 6*RIGHT)
        self.wait(2)
        self.play(FadeOut(par_mean))
        self.wait(1)
        self.play(ReplacementTransform(function_code, code))
        self.wait(1)
        self.play(code.shift, 2*UP)
        self.play(code.shift, 2*LEFT)
        self.wait(1)
        self.play(code[2][1].shift, 1*DOWN)
        self.play(code[2][1].shift, 1*LEFT)
        self.wait(2)
        self.play(Write(topics_array[0]), run_time=1)
        self.play(topics_array[0].shift, 4*RIGHT)
        self.play(topics_array[0].shift, 0.5*UP)
        self.wait(1)
        self.play(ReplacementTransform(topics_array[0], topics_array[1]))
        self.play(code[2][1].shift, 0.8*DOWN)
        self.play(topics_array[1].shift, 4*RIGHT)
        self.play(topics_array[1].shift, 0.5*UP)
        self.wait(1)
        self.play(ReplacementTransform(topics_array[1], topics_array[2]))
        self.play(code[2][1].shift, 0.6*DOWN)
        self.play(topics_array[2].shift, 4*RIGHT)
        self.play(topics_array[2].shift, 0.5*UP)
        self.wait(3)







