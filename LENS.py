from manim import *


class LENS(MovingCameraScene):
    def construct(self):
        p = (
            [-5, 2, 0],
            [-5, 0, 0],
            [0, 0, 0],
            [2.5, -1, 0],
            [2.5, 0, 0],
            [0, 2, 0],
            [5 / 3, 0, 0],
        )
        ## init
        mainline = (
            DashedLine([-10, 0, 0], [10, 0, 0], stroke_width=2),
            DashedLine([0, 10, 0], [0, -10, 0], stroke_width=2),
        )
        ratio = 0.5
        lens = (
            Arc(
                arc_center=[-4, 0, 0],
                angle=np.arctan(ratio),
                radius=np.sqrt(20),
                stroke_width=2,
            ),
            Arc(
                arc_center=[4, 0, 0],
                angle=np.arctan(ratio),
                start_angle=PI,
                radius=np.sqrt(20),
                stroke_width=2,
            ),
            Arc(
                arc_center=[-4, 0, 0],
                angle=np.arctan(ratio),
                start_angle=2 * PI - np.arctan(ratio),
                radius=np.sqrt(20),
                stroke_width=2,
            ),
            Arc(
                arc_center=[4, 0, 0],
                angle=np.arctan(ratio),
                start_angle=PI - np.arctan(ratio),
                radius=np.sqrt(20),
                stroke_width=2,
            ),
        )
        self.play(FadeIn(lens[0]), FadeIn(lens[1]), FadeIn(lens[2]), FadeIn(lens[3]))
        for i in mainline:
            self.play(Create(i))
        candle = Arrow([-5, -0.25, 0], [-5, 2.25, 0])
        image = Arrow([2.5, 0.25, 0], [2.5, -1.25, 0])
        self.play(Create(candle), Create(image))

        ## text1
        A, B, AA, BB, O = [
            MathTex(tex).scale(0.75) for tex in ["A", "B", "A'", "B'", "O"]
        ]
        A.next_to(p[0], LEFT * 0.35 + UP * 0.35)
        B.next_to(p[1], LEFT * 0.35 + DOWN * 0.35)
        AA.next_to(p[3], RIGHT * 0.35 + DOWN * 0.35)
        BB.next_to(p[4], RIGHT * 0.35 + UP * 0.35)
        O.next_to(p[2], DOWN * 0.35)
        self.play(Write(A), Write(B), Write(AA), Write(BB), Write(O))

        self.wait(0.5)

        ## line
        line = (
            Line(p[0], p[3], stroke_width=2),
            Line(p[0], p[5], stroke_width=2),
            Line(p[5], p[3], stroke_width=2),
            Line(p[1], p[2], stroke_width=2),
            Line(p[4], p[2], stroke_width=2),
            Line(p[5], p[2], stroke_width=2),
            Line(p[0], p[1], stroke_width=2),
            Line(p[3], p[4], stroke_width=2),
        )
        self.play(
            Create(line[0]),
            Create(line[1]),
            Create(line[2]),
            Create(line[3]),
            Create(line[4]),
            Create(line[5]),
            Create(line[6]),
            Create(line[7]),
            run_time=0.5,
        )

        self.wait(0.25)

        ## text2
        C, F = [MathTex(tex).scale(0.75) for tex in ["C", "F"]]
        C.next_to(p[5], RIGHT * 0.35 + UP * 0.35)
        F.next_to(p[6], RIGHT * 0.35 + UP * 0.35)
        self.play(Write(C), Write(F))

        ## delete
        self.play(FadeOut(candle), FadeOut(image))
        self.play(
            FadeOut(mainline[0]),
            FadeOut(mainline[1]),
            FadeOut(lens[0]),
            FadeOut(lens[1]),
            FadeOut(lens[2]),
            FadeOut(lens[3]),
        )

        ## text3
        u = MathTex("BO=u").scale(1)
        v = MathTex("OB'=v").scale(1)
        f = MathTex("OF=f").scale(1)
        u.move_to([-3.5, -2, 0])
        v.next_to(u, 2 * RIGHT, aligned_edge=LEFT)
        f.next_to(v, 2 * RIGHT, aligned_edge=LEFT)
        self.play(Write(u), Write(v), Write(f))
        self.wait(2)
        ## camera
        self.play(self.camera.frame.animate.set(width=20))
        self.play(self.camera.frame.animate.move_to([3, 0, 0]))

        ## prove
        step1 = MathTex(r"\because", r"\angle AOB = \angle A'OB'")
        step1.scale(1).move_to([7, 5, 0])
        step2 = MathTex(r"\angle ABO = \angle A'B'O")
        step2.scale(1).next_to(step1, DOWN, aligned_edge=RIGHT)
        step3 = MathTex(r"\therefore", r"\triangle AOB \sim  \triangle A'OB'")
        step3.scale(1).next_to(step1, DOWN * 3.35, aligned_edge=LEFT)
        step4 = MathTex(
            r"\therefore",
            r"AB : A'B' = OB : OB'",
            substrings_to_isolate=[r"\therefore"],
        )
        step4.scale(1).next_to(step3, DOWN, aligned_edge=LEFT)
        self.play(Write(step1))
        self.play(Write(step2))
        self.play(Write(step3))
        self.play(Write(step4))
        step5 = MathTex(r"\because", r"\angle CFO = \angle A'FB'")
        step5.scale(1).next_to(step4, DOWN, aligned_edge=LEFT)
        step6 = MathTex(r"\angle COF = \angle A'B'F")
        step6.scale(1).next_to(step5, DOWN, aligned_edge=RIGHT)
        step7 = MathTex(r"\therefore", r"\triangle CFO \sim  \triangle A'FB'")
        step7.scale(1).next_to(step5, DOWN * 3.35, aligned_edge=LEFT)
        step8 = MathTex(
            r"\therefore",
            r"CO : A'B' = OF : B'F",
            substrings_to_isolate=[r"\therefore"],
        )
        step8.scale(1).next_to(step7, DOWN, aligned_edge=LEFT)
        self.play(Write(step5))
        self.play(Write(step6))
        self.play(Write(step7))
        self.play(Write(step8))
        self.play(
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step3),
            FadeOut(step5),
            FadeOut(step6),
            FadeOut(step7),
        )
        self.play(
            step4.animate.move_to([7, 5, 0]),
        )
        self.play(step8.animate.next_to(step4, DOWN, aligned_edge=LEFT))
        self.play(
            FadeOut(step8.get_part_by_tex("\\therefore")),
            FadeOut(step4.get_part_by_tex("\\therefore")),
        )
        step9 = MathTex(r"\because", r"\text{四边形}", r"ABOC", r"\text{是矩形}")
        step9.scale(1).next_to(step8, DOWN, aligned_edge=LEFT)
        step10 = MathTex(r"\therefore", r"AB = CO", substrings_to_isolate=["AB", "CO"])
        step10.scale(1).next_to(step9, DOWN, aligned_edge=LEFT)
        step11 = MathTex(
            r"\therefore",
            r"AB : A'B' = OF : B'F",
            substrings_to_isolate=["AB", "A'B'", "OF", "B'F"],
        )
        step11.scale(1).next_to(step10, DOWN, aligned_edge=LEFT)
        step12 = MathTex(r"\therefore", r"\frac{u}{v} = \frac{f}{v-f}")
        step12.scale(1).next_to(step11, DOWN, aligned_edge=LEFT)
        step13 = MathTex(r"\therefore", "u (v - f) = vf")
        step13.scale(1).next_to(step12, DOWN, aligned_edge=LEFT)
        step14 = MathTex(r"\therefore", "uv - uf = vf ")
        step14.scale(1).next_to(step13, DOWN, aligned_edge=LEFT)
        step15 = MathTex(
            r"\therefore", r"\frac{uv}{uvf} - \frac{uf}{uvf} = \frac{vf}{uvf}"
        )
        step15.scale(1).next_to(step14, DOWN, aligned_edge=LEFT)
        step16 = MathTex(r"\text{化简，得：}")
        step16.scale(1).next_to(step15, DOWN, aligned_edge=LEFT)
        step17 = MathTex(r"\frac{1}{u} + \frac{1}{v} = \frac{1}{f}")
        step17.scale(1).next_to(step16, DOWN, aligned_edge=LEFT)
        self.play(Write(step9))
        self.play(Write(step10))
        self.play(Write(step11))
        self.add(step11).play(TransformFromCopy(step11, step12))
        self.wait(0.5)
        self.add(step12).play(TransformFromCopy(step12, step13))
        self.wait(0.5)
        self.add(step13).play(TransformFromCopy(step13, step14))
        self.wait(0.5)
        self.add(step14).play(TransformFromCopy(step14, step15))
        self.wait(0.5)
        self.play(Write(step16))
        self.wait(0.5)
        self.play(Write(step17))
        self.play(step17.animate.scale(2))
        self.play(step17.animate.scale(0.5))
        self.wait(2)