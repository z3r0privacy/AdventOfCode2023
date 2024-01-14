using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AOC2023_net
{
    abstract class AbstractDay
    {
        public int Day { get; private set; }
        public string FilePath { get; private set; }
        public abstract bool Done { get; }

        public AbstractDay()
        {
            Day = int.Parse(GetType().Name[^2..]);
            FilePath = Path.GetFullPath($"..\\..\\..\\..\\..\\Inputs\\{Day}.txt");
        }

        public async Task<string> ReadFile()
        {
            return await File.ReadAllTextAsync(FilePath);
        }

        public async Task<IEnumerable<string>> ReadFileLines(bool strip=true)
        {
            var result = new List<string>();
            await foreach(var line in File.ReadLinesAsync(FilePath))
            {
                if (strip && string.IsNullOrEmpty(line)) continue;
                result.Add(line);
            }
            return result;
        }

        public async Task<IEnumerable<int>> ReadFileLinesAsNum()
        {
            return (await ReadFileLines()).Select(int.Parse);
        }

        public async Task<string> TrySolve1()
        {
            try
            {
                return await SolvePart1();
            }
            catch (NotImplementedException)
            {
                return "Not yet implemented";
            }
        }

        public async Task<string> TrySolve2()
        {
            try
            {
                return await SolvePart2();
            }
            catch (NotImplementedException)
            {
                return "Not yet implemented";
            }
        }

        public abstract Task<string> SolvePart1();
        public abstract Task<string> SolvePart2();
    }
}
