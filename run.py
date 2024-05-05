from html2rl.rlconversions import cleanHTML, toRParagraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

rte_text = '<ul><li style="color: rgb(0, 0, 0)"><p><span style="color: rgb(0, 0, 0)"><strong>Projects </strong>are worth mentioning when they are standout, and when they add to your resume. When you have strong and relevant work experience, they are less important. Describe the impact, the challenges and why the project stands out. Blogs and articles can also be projects.</span></p></li><li><p><span style="color: rgb(0, 0, 0)"><strong>Technical blogging</strong> on</span><u><span style="color: rgb(17, 85, 204)"> The Pragmatic Engineer blog</span></u><span style="color: rgb(0, 0, 0)">. Popular articles include a piece on Angular Material and one on Clean Code.</span></p></li></ul>'

rl_para_txt = cleanHTML(rte_text, "Helvetica-BoldOblique")

obj = toRParagraph(rl_para_txt, normal_style=styles["Normal"])
print(type(obj))