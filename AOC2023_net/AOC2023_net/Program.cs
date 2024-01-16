
using AOC2023_net;

var days = new AbstractDay[] { new Day13(), new Day14() };

foreach (var d in days.Where(d => !d.Done))
{
    Console.WriteLine($"######### Day {d.Day} #########");
    var start = DateTime.Now;
    var sol1 = await d.TrySolve1();
    var sol2 = await d.TrySolve2();
    var duration = DateTime.Now - start;
    Console.WriteLine($"Solution 1: {sol1}");
    Console.WriteLine($"Solution 2: {sol2}");
    Console.WriteLine($"######### {duration} #########");
    Console.WriteLine();
}


foreach (var d in days.Where(d => d.Done))
{
    Console.WriteLine($"######### Day {d.Day} #########");
    var start = DateTime.Now;
    var sol1 = await d.TrySolve1();
    var sol2 = await d.TrySolve2();
    var duration = DateTime.Now - start;
    Console.WriteLine($"Solution 1: {sol1}");
    Console.WriteLine($"Solution 2: {sol2}");
    Console.WriteLine($"######### {duration} #########");
    Console.WriteLine();
}
