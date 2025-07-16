from PyPDF2 import PdfMerger

merger = PdfMerger()

# first PDF
# relative file path to pdf
merger.append("PDF merger/JoshuaMcleod_Resume.pdf")
# second appended pdf
merger.append("##redacted")
# third appended pdf
merger.append("##redacted")


merger.write("PDF merger//merged.pdf")  # output file
merger.close()
