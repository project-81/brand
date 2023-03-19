# brand

Brand assets for project-81.

## Getting Started

Workflow tasks use [mklib](https://pypi.org/project/vmklib/)'s `mk`
command-line entry-point.

Ensure that [Python](https://www.python.org/) is already installed on your
system. Install the package with:

```
pip[3] install [--user] vmklib
```

Note that `[]` indicates optional information, depending on your system. It can
alternatively be installed system-wide via:

```
sudo[3] -H pip install vmklib
```

## Generating Scalable Vector Graphics

*What are [SVG](https://www.w3.org/TR/SVG2/)'s?*

A Python project called [svgen](https://pypi.org/project/svgen/) is used
to compose vector graphics for brand assets.

Run `mk svg-{script}`, where `script` corresponds to a pair of `.py` and
`.json` files in the `svg_scripts` directory in the root of the repository.

Example: `mk svg-logo`.

This generates an SVG file in `build/svg`.

Running `mk images-{script}` will append a `--images` argument to the
command-line invocation that will cause `svgen` to invoke various
[Inkscape](https://inkscape.org/) commands to generate `.png` image files
of various sizes (depending on the underlying size and aspect ratio of the
source).
