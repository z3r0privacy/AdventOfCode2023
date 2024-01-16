using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AOC2023_net
{
    internal class Day14 : AbstractDay
    {
        public override bool Done => true;

        private void Flip(List<char[]> field)
        {
            for (var i = 1; i < field.Count; i++)
            {
                for (var j = 0; j < field[i].Length; j++)
                {
                    if (field[i][j] == 'O')
                    {
                        int y;
                        for (y = i - 1; y >= 0; y--)
                        {
                            if (field[y][j] != '.')
                            {
                                break;
                            }
                        }
                        ++y;
                        if (y != i)
                        {
                            field[y][j] = 'O';
                            field[i][j] = '.';
                        }
                    }
                }
            }
        }

        private int CalcValue(List<char[]> field)
        {
            var mult = 1;
            var sum = 0;
            for (var i = field.Count - 1; i >= 0; i--)
            {
                sum += mult * field[i].Count(c => c == 'O');
                ++mult;
            }
            return sum;
        }

        public override async Task<string> SolvePart1()
        {
            var field = (await ReadFileLines()).Select(s => s.ToCharArray()).ToList();
            Flip(field);
            var sum = CalcValue(field);
            return sum.ToString();
        }

        private List<char[]> RotRight(List<char[]> field)
        {
            var rField = new List<char[]>();
            for (var i = 0; i < field[0].Length; i++)
            {
                rField.Add(new char[field.Count]);
            }
            for (var i = 0; i < field.Count; i++)
            {
                for (var j = 0; j < field[i].Length; j++)
                {
                    rField[j][rField[j].Length - i - 1] = field[i][j];
                }
            }
            return rField;
        }

        private List<char[]> DoRound(List<char[]> field)
        {
            Flip(field);
            field = RotRight(field);
            Flip(field);
            field = RotRight(field);
            Flip(field);
            field = RotRight(field);
            Flip(field);
            field = RotRight(field);
            return field;
        }

        private List<char[]> Copy(List<char[]> orig)
        {
            var cpy = new List<char[]>();
            foreach (var l in orig)
            {
                var a = new char[l.Length];
                for (var i = 0; i < l.Length; i++)
                {
                    a[i] = l[i];
                }
                cpy.Add(a);
            }
            return cpy;
        }

        private bool FieldEqual(List<char[]> a, List<char[]> b)
        {
            if (a == b) return true;
            if (a.Count != b.Count) return false;
            for (var i = 0; i < a.Count; i++)
            {
                if (a[i].Length != b[i].Length) return false;
                for (var j = 0; j < a[i].Length; j++)
                {
                    if (a[i][j] != b[i][j]) return false;
                }
            }
            return true;
        }

        private int FieldInList(List<List<char[]>> list, List<char[]> field)
        {
            var idx = 0;
            foreach(var l in list)
            {
                if (FieldEqual(l, field)) return idx;
                ++idx;
            }
            return -1;
        }

        public override async Task<string> SolvePart2()
        {
            var cycles = 1000000000;
            var field = (await ReadFileLines()).Select(s => s.ToCharArray()).ToList();
            var rounds = 0;
            var states = new List<List<char[]>>();
            var sum = CalcValue(field);
            states.Add(Copy(field));
            int idx;
            while (true)
            {
                field = DoRound(field);
                ++rounds;
                idx = FieldInList(states, field);
                if (idx >= 0)
                {
                    break;
                }
                states.Add(Copy(field));
            }
            var rem = cycles - rounds;
            var interval = rounds - idx;
            rounds += (rem / interval) * interval;
            for (; rounds < cycles; rounds++)
            {
                field = DoRound(field);
            }

            return CalcValue(field).ToString();
        }
    }
}
