#! /usr/bin/python3

import sys
import re

if len(sys.argv) < 3:
    print("Usage: ./convert.py templated.html result.html")
    exit()
inputFilepath = sys.argv[1]
outputFilepath = sys.argv[2]

with open(inputFilepath, 'r') as inputFile:
    data = inputFile.read()


result = re.sub('<scr-tip.*?usefulness=[\'"](.*?)[\'"].*?importance=[\'"](.*?)[\'"]>.*?<tip-title>(.*?)</tip-title>.*?<tip-desc>(.*?)</tip-desc>.*?</scr-tip>',
        r"""<div class="card is-fullwidth">
    <header class="card-header">
        <div style="padding: 10px; display:flex; justify-content:center; align-items:center; text-align:center;">
            Usefulness: \1
            <br>
            Importance: \2
        </div>
        <div class="card-header-title">\3</div>
        <a class="card-header-icon card-toggle">
             Detailed description&nbsp;<i class="fas fa-angle-down"></i>
        </a>
    </header>
    <div class="card-content is-hidden">
        <div class="content">
            \4
        </div>
    </div>
</div>""", data, flags=re.DOTALL)

result = re.sub('<scr-contribute>',
        r"""<div class="box">
                <div class="media">
                    <div class="media-left">
                        <img class="image is-32x32" src="../images/GitHub-Mark-120px-plus.png" alt="GitHub Mark">
                    </div>
                    <div class="media-content is-size-5 has-text-centered">
                        <a href="https://github.com/gw2scratch/tips">Contribute on GitHub</a>
                    </div>
                </div>
            </div>""", result)

with open(outputFilepath, 'w') as outputFile:
    outputFile.write(result)
