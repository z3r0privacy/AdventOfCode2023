using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AOC2023_net
{
    internal class Day16 : AbstractDay
    {
        public override bool Done => true;

        private int CountEnergizedFields(List<string> field, int startX, int startY, char startD)
        {
            var visitedNodes = new HashSet<(int x, int y, char d)>();
            var queue = new Queue<(int x, int y, char d)>();
            var moveDirs = new Dictionary<char, (int x, int y)>
            {
                {'r', (1, 0) },
                {'d', (0, 1) },
                {'l', (-1, 0) },
                {'u', (0, -1) },
            };
            queue.Enqueue((startX, startY, startD));
            while (queue.Count > 0)
            {
                var b = queue.Dequeue();
                if (visitedNodes.Contains(b)) continue;
                if (b.x < 0 || b.y < 0 || b.y >= field.Count || b.x >= field[b.y].Length) continue;

                visitedNodes.Add(b);
                switch (field[b.y][b.x])
                {
                    case '.':
                        queue.Enqueue((b.x + moveDirs[b.d].x, b.y + moveDirs[b.d].y, b.d));
                        break;
                    case '/':
                        {
                            switch (b.d)
                            {
                                case 'r':
                                    queue.Enqueue((b.x, b.y - 1, 'u'));
                                    break;
                                case 'd':
                                    queue.Enqueue((b.x - 1, b.y, 'l'));
                                    break;
                                case 'l':
                                    queue.Enqueue((b.x, b.y + 1, 'd'));
                                    break;
                                case 'u':
                                    queue.Enqueue((b.x + 1, b.y, 'r'));
                                    break;
                            }
                            break;
                        }
                    case '\\':
                        {
                            switch (b.d)
                            {
                                case 'r':
                                    queue.Enqueue((b.x, b.y + 1, 'd'));
                                    break;
                                case 'd':
                                    queue.Enqueue((b.x + 1, b.y, 'r'));
                                    break;
                                case 'l':
                                    queue.Enqueue((b.x, b.y - 1, 'u'));
                                    break;
                                case 'u':
                                    queue.Enqueue((b.x - 1, b.y, 'l'));
                                    break;
                            }
                            break;
                        }
                    case '|':
                        switch (b.d)
                        {
                            case 'u':
                            case 'd':
                                queue.Enqueue((b.x + moveDirs[b.d].x, b.y + moveDirs[b.d].y, b.d));
                                break;
                            case 'l':
                            case 'r':
                                queue.Enqueue((b.x, b.y + 1, 'd'));
                                queue.Enqueue((b.x, b.y - 1, 'u'));
                                break;
                        }
                        break;
                    case '-':
                        switch (b.d)
                        {
                            case 'l':
                            case 'r':
                                queue.Enqueue((b.x + moveDirs[b.d].x, b.y + moveDirs[b.d].y, b.d));
                                break;
                            case 'u':
                            case 'd':
                                queue.Enqueue((b.x - 1, b.y, 'l'));
                                queue.Enqueue((b.x + 1, b.y, 'r'));
                                break;
                        }
                        break;
                }
            }
            return new HashSet<(int, int)>(visitedNodes.Select(b => (b.x, b.y))).Count;

        }

        public override async Task<string> SolvePart1()
        {
            var field = (await ReadFileLines()).ToList();
            return CountEnergizedFields(field, 0, 0, 'r').ToString();
        }

        public override async Task<string> SolvePart2()
        {
            var field = (await ReadFileLines()).ToList();
            var max = 0;
            for (var y = 0; y < field.Count; y++)
            {
                var energized = CountEnergizedFields(field, 0, y, 'r');
                if (energized > max) max = energized;
                energized = CountEnergizedFields(field, field[y].Length - 1, y, 'l');
                if (energized > max) max = energized;
            }
            for (var x = 0; x < field[0].Length; x++)
            {
                var energized = CountEnergizedFields(field, x, 0, 'd');
                if (energized > max) max = energized;
                energized = CountEnergizedFields(field, x, field.Count-1, 'u');
                if (energized > max) max = energized;
            }
            return max.ToString();
        }
    }
}
