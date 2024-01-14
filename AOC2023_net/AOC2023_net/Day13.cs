using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.XPath;

namespace AOC2023_net
{
    internal class Day13 : AbstractDay
    {
        public override bool Done => true;

        private bool FindHorMirror(List<char[]> lines, int start, int end, out int pos, int blocked_pos = -1)
        {
            pos = -1;
            for (var i = 1; i < (end-start); i++)
            {
                var mirr_found = true;
                for (var j = 0; mirr_found && j < lines[start].Length; j++)
                {
                    var d = 0;
                    while (d < i && d < end-start-i && mirr_found)
                    {
                        if (lines[start + i - 1 - d][j] != lines[start + i + d][j])
                        {
                            mirr_found = false;
                        }
                        ++d;
                    }
                }
                if (mirr_found && i != blocked_pos)
                {
                    pos = i;
                    return true;
                }
            }
            return false;
        }

        private bool FindVerMirror(List<char[]> lines, int start, int end, out int pos, int blocked_pos=-1)
        {
            pos = -1;
            for (var i = 1; i < lines[start].Length; i++)
            {
                var mirr_found = true;
                for (var j = 0; mirr_found && j < (end - start); j++)
                {
                    var d = 0;
                    while (d < i && d < lines[start].Length - i && mirr_found)
                    {
                        // i = x
                        // j = y
                        if (lines[start + j][i-1-d] != lines[start + j][i+d])
                        {
                            mirr_found = false;
                        }
                        ++d;
                    }
                }
                if (mirr_found && i != blocked_pos)
                {
                    pos = i;
                    return true;
                }
            }
            return false;
        }

        private Dictionary<int, string> Task1Results { get; set; } = [];

        public override async Task<string> SolvePart1()
        {
            var lines = (await ReadFileLines(false)).Select(s => s.ToCharArray()).ToList();
            if (lines[^1].Length != 0)
            {
                lines.Add([]);
            }
            var curr_idx = 0;
            var result = 0;
            while (curr_idx < lines.Count)
            {
                var end = curr_idx;
                while (lines[end].Length != 0) end++;

                int pos;
                if (FindHorMirror(lines, curr_idx, end, out pos))
                {
                    result += 100 * pos;
                    Task1Results[curr_idx] = $"hor{pos}";
                }
                else if (FindVerMirror(lines, curr_idx, end, out pos))
                {
                    result += pos;
                    Task1Results[curr_idx] = $"ver{pos}";
                }
                else
                {
                    throw new InvalidOperationException("No Mirror found");
                }

                curr_idx = end + 1;
            }
            return result.ToString();
        }

        public override async Task<string> SolvePart2()
        {
            var lines = (await ReadFileLines(false)).Select(s => s.ToCharArray()).ToList();
            if (lines[^1].Length != 0)
            {
                lines.Add([]);
            }
            var curr_idx = 0;
            var result = 0;
            while (curr_idx < lines.Count)
            {
                var end = curr_idx;
                while (lines[end].Length != 0) end++;

                var bv = -1;
                var bh = -1;
                if (Task1Results[curr_idx].StartsWith("ver"))
                {
                    bv = int.Parse(Task1Results[curr_idx][3..]);
                } else
                {
                    bh = int.Parse(Task1Results[curr_idx][3..]);
                }

                var found = false;
                for (var i = 0; !found && i < (end - curr_idx) * lines[curr_idx].Length; i++)
                {
                    var sl = i / lines[curr_idx].Length;
                    var sr = i % lines[curr_idx].Length;
                    lines[curr_idx + sl][sr] = lines[curr_idx + sl][sr] == '#' ? '.' : '#';
                    if (FindHorMirror(lines, curr_idx, end, out int pos, blocked_pos: bh))
                    {
                        result += 100 * pos;
                        found = true;
                    }
                    else if (FindVerMirror(lines, curr_idx, end, out pos, blocked_pos: bv))
                    {
                        result += pos;
                        found = true;
                    }
                    else
                    {

                    }
                    lines[curr_idx + sl][sr] = lines[curr_idx + sl][sr] == '#' ? '.' : '#';
                }
                if (!found)
                {
                    throw new InvalidOperationException("No smudged Mirror found");
                }
                curr_idx = end + 1;
            }
            return result.ToString();
        }
    }
}
