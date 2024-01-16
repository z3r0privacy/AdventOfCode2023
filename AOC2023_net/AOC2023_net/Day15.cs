using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AOC2023_net
{
    internal class Day15 : AbstractDay
    {
        public override bool Done => true;

        private byte CalcHash(string s)
        {
            byte h = 0;
            foreach (var c in s)
            {
                h += (byte)c;
                h *= 17;
            }
            return h;
        }

        public override async Task<string> SolvePart1()
        {
            var input = (await ReadFile()).Trim();
            var sum = 0;
            foreach (var s in input.Split(","))
            {
                sum += CalcHash(s);
            }
            return sum.ToString();
        }

        public override async Task<string> SolvePart2()
        {
            var boxes = new List<(string label, int focal)>[256];
            for (var i = 0; i < 256; i++)
            {
                boxes[i] = [];
            }
            foreach (var instr in (await ReadFile()).Split(","))
            {
                if (instr.Contains('='))
                {
                    var lbl = instr.Split('=')[0];
                    var val = int.Parse(instr.Split("=")[1]);
                    var box = CalcHash(lbl);
                    var replaced = false;
                    for (var i = 0; i < boxes[box].Count; i++)
                    {
                        if (boxes[box][i].label == lbl)
                        {
                            boxes[box][i] = (lbl, val);
                            replaced = true;
                            break;
                        }
                    }
                    if (!replaced)
                    {
                        boxes[box].Add((lbl, val));
                    }
                } else
                {
                    var idx = -1;
                    var lbl = instr.Split('-')[0];
                    var box = CalcHash(lbl);
                    for (var i = 0; i < boxes[box].Count; i++)
                    {
                        if (boxes[box][i].label == lbl)
                        {
                            idx = i;
                            break;
                        }
                    }
                    if (idx >= 0)
                    {
                        boxes[box].RemoveAt(idx);
                    }
                }
            }
            var sum = 0;
            for (var b = 0; b < 256; b++)
            {
                for (var i = 0; i < boxes[b].Count; i++)
                {
                    sum += (b + 1) * (i + 1) * boxes[b][i].focal;
                }
            }
            return sum.ToString();
        }
    }
}
