from pathlib import Path
import os
from flip import parser, main, DISPLAY_TITLE
from wand.image import Image
import hashlib

def create_test_image(test_img, width, height):
    with open(test_img, "w") as f:
        f.write("P1\n")
        f.write("# test image\n")
        f.write("%s %s\n" % (width, height))
        line = " ".join("0" for x in range(width))

        for i, e in enumerate(range(height)):
            line = ("1" if i == 0 else "0") + line[1:]
            f.write(line + "\n")
        f.write("EOF\n")

def read_contents(fn):
    with open(fn, "r") as f:
        return "".join(f.readlines()).encode("utf-8")

def test_main(mocker, tmp_path: Path):
    """
    Simulated test run of the app.
    """
    inputdir = tmp_path / 'incoming'
    outputdir = tmp_path / 'outgoing'
    inputdir.mkdir()
    outputdir.mkdir()

    test_img = os.path.join(inputdir, "test.ppm")
    create_test_image(test_img, 24, 2)

    for d in ["horizontal", "vertical", "both"]:
        options = parser.parse_args([d])

        main(options, inputdir, outputdir)

        assert os.listdir(inputdir) == os.listdir(outputdir)

        infile = os.path.join(inputdir, "test.ppm")
        outfile = os.path.join(outputdir, "test.ppm")
        with Image(filename= outfile) as i:
            assert i.width == 24
            assert i.height == 2

        assert hashlib.md5(read_contents(infile)).hexdigest() != hashlib.md5(read_contents(outfile)).hexdigest()
