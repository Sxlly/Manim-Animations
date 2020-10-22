#!/user/bin/env python

from big_ol_pile_of_manim_imports import *
import numpy as np


class Arrays(Scene):

    def construct(self):
        
        list_obj = IntegerMatrix([(1,2,3,4,5)])
        list_obj.scale(2)

        array_obj = IntegerMatrix([(1,2,3),(4,5,6)])
        array_obj.scale(2)
        array_cp = array_obj.copy()

        array_nums1 = array_obj[0:1][0:3]

        shift_matrix = [[1.0, 0.5], [1.0, 0.0]]
        shift_matrix2 =[[0.85, 0.0], [0.5, 0.0]]

        oned_text = TextMobject("1 Dimensional")
        oned_text.scale(1)

        twod_text = TextMobject("2 Dimensional")
        twod_text.scale(1)

        threed_text = TextMobject("3 Dimensional")
        threed_text.scale(1)

        x_axis = Arrow(list_obj[0][0], list_obj[0][4]).set_color(RED)
        x_axis.scale(0.85)

        depth_square = Rectangle(width=7, height=3).set_color(PURPLE)
        depth_square.scale(0.5)

        depth_square2 = depth_square.copy()
        depth_square3 = depth_square.copy()

        x_axis_text = TextMobject("Length").set_color(RED)
        x_axis_text.scale(1)

        y_axis_text = TextMobject("Width").set_color(YELLOW)
        y_axis_text.scale(1)

        z_axis_text = TextMobject("Depth").set_color(PURPLE)
        z_axis_text.scale(1)

        row_text = TextMobject("Row").set_color(RED)
        col_text = TextMobject("Column").set_color(YELLOW)

        element_text = TextMobject("Element").set_color(BLUE)


        self.play(Write(list_obj), run_time=2)
        self.wait(2)
        self.wait(1)
        self.play(ApplyMethod(list_obj.scale, 0.75))
        self.wait(1)
        self.play(list_obj.shift, 1*UP)
        self.wait(1)
        self.play(Write(element_text), run_time=1)
        self.play(ApplyMethod(list_obj[0][0:5].set_color, BLUE))
        self.play(element_text.shift, 1*DOWN)
        self.wait(1)
        self.play(Write(x_axis), run_time=2)
        self.play(x_axis.shift, 2*UP)
        self.wait(1)
        self.play(FadeIn(x_axis_text))
        self.play(x_axis_text.shift, 2.5*UP)
        self.wait(1)
        self.play(Write(oned_text), run_time=2)
        self.wait(2)
        self.play(FadeOutAndShiftDown(x_axis), FadeOutAndShiftDown(element_text))
        self.play(ReplacementTransform(oned_text, twod_text))
        self.play(twod_text.shift, 3*DOWN)
        self.play(ReplacementTransform(list_obj, array_obj))
        self.play(Write(y_axis_text), run_time=1)
        self.play(y_axis_text.shift, 5*LEFT)
        self.wait(1)
        self.play(ReplacementTransform(x_axis_text, row_text), ReplacementTransform(y_axis_text, col_text))
        self.play(row_text.shift, 2.5*UP, col_text.shift, 5*LEFT)
        self.wait(1)
        self.play(FadeOut(row_text), FadeOut(col_text))
        self.play(Write(array_cp), run_time=1)
        self.play(ApplyMethod(array_obj.scale, 0.5), ApplyMethod(array_cp.scale, 0.5))
        self.play(ApplyMethod(array_obj.shift, 2*LEFT), ApplyMethod(array_cp.shift, 2*RIGHT))
        self.play(ReplacementTransform(twod_text, threed_text))
        self.play(threed_text.shift, 3*UP)
        self.play(ApplyMatrix(shift_matrix, array_obj), ApplyMatrix(shift_matrix, array_cp))
        self.wait(1)
        self.play(ApplyMethod(array_obj.shift, 3*RIGHT), ApplyMethod(array_cp.shift, 3*LEFT))
        self.play(ApplyMethod(array_cp.shift, 2*DOWN), ApplyMethod(array_obj.shift, 1*UP))
        self.play(ShowCreation(depth_square), ShowCreation(depth_square2), ShowCreation(depth_square3))
        self.play(ApplyMatrix(shift_matrix, depth_square), ApplyMatrix(shift_matrix, depth_square2), ApplyMatrix(shift_matrix, depth_square3))
        self.play(ApplyMethod(depth_square.shift, 0.5*DOWN), ApplyMethod(depth_square2.shift, 0.5*DOWN), ApplyMethod(depth_square3.shift, 0.5*DOWN))
        self.play(ApplyMethod(depth_square.shift, 0.4*RIGHT), ApplyMethod(depth_square2.shift, 0.4*RIGHT), ApplyMethod(depth_square3.shift, 0.4*RIGHT))
        self.play(ApplyMethod(depth_square2.shift, 0.5*UP), ApplyMethod(depth_square3.shift, 0.75*UP))
        self.play(ApplyMethod(depth_square2.shift, 0.4*LEFT), ApplyMethod(depth_square3.shift, 0.6*LEFT))
        self.play(ApplyMethod(depth_square2.shift, 0.4*DOWN), ApplyMethod(depth_square3.shift, 0.4*DOWN))
        self.play(ApplyMethod(depth_square.shift, 0.4*RIGHT), ApplyMethod(depth_square3.shift, 0.4*LEFT))
        self.play(Rotate(array_obj, PI/4, about_point=RIGHT), Rotate(array_cp, PI/4, about_point=RIGHT), Rotate(depth_square, PI/4, about_point=RIGHT), Rotate(depth_square2, PI/4, about_point=RIGHT), Rotate(depth_square3, PI/4, about_point=RIGHT))
        self.play(ApplyMethod(array_obj.shift, 0.5*UP))
        self.play(ApplyMethod(array_obj.shift, 2*RIGHT), ApplyMethod(array_cp.shift, 2*LEFT), ApplyMethod(depth_square.shift, 1.5*RIGHT), ApplyMethod(depth_square3.shift, 1.5*LEFT))
        self.play(Write(z_axis_text), run_time=1)
        self.play(z_axis_text.shift, 1.5*DOWN + 5*LEFT)
        self.play(array_nums1.shift, 1.2*LEFT + 0.15*DOWN)
        self.play(array_nums1.shift, 2.2*LEFT + 0.3*DOWN)
        self.play(array_nums1.shift, 2.2*LEFT + 0.4*DOWN)
        self.play(FadeOut(array_nums1), FadeOut(array_obj), FadeOut(array_cp), FadeOut(depth_square), FadeOut(depth_square2), FadeOut(depth_square3), FadeOut(z_axis_text), FadeOut(threed_text))
        self.wait(3)


