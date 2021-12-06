# Scroll to the bottom to see the actual code

#
$PuzzleData = @"
1,1,1,3,3,2,1,1,1,1,1,4,4,1,4,1,4,1,1,4,1,1,1,3,3,2,3,1,2,1,1,1,1,1,1,1,3,4,1,1,4,3,1,2,3,1,1,1,5,2,1,1,1,1,2,1,2,5,2,2,1,1,1,3,1,1,1,4,1,1,1,1,1,3,3,2,1,1,3,1,4,1,2,1,5,1,4,2,1,1,5,1,1,1,1,4,3,1,3,2,1,4,1,1,2,1,4,4,5,1,3,1,1,1,1,2,1,4,4,1,1,1,3,1,5,1,1,1,1,1,3,2,5,1,5,4,1,4,1,3,5,1,2,5,4,3,3,2,4,1,5,1,1,2,4,1,1,1,1,2,4,1,2,5,1,4,1,4,2,5,4,1,1,2,2,4,1,5,1,4,3,3,2,3,1,2,3,1,4,1,1,1,3,5,1,1,1,3,5,1,1,4,1,4,4,1,3,1,1,1,2,3,3,2,5,1,2,1,1,2,2,1,3,4,1,3,5,1,3,4,3,5,1,1,5,1,3,3,2,1,5,1,1,3,1,1,3,1,2,1,3,2,5,1,3,1,1,3,5,1,1,1,1,2,1,2,4,4,4,2,2,3,1,5,1,2,1,3,3,3,4,1,1,5,1,3,2,4,1,5,5,1,4,4,1,4,4,1,1,2
"@
#>

<#
$PuzzleData = @"
3,4,3,1,2
"@
#>

class Lanternfish {
    [int[]]$Ages
    [int]$NewAge = 8
    [int]$ResetAge = 6
    [int]$ReproduceAge = 0

    Lanternfish() {
        $this.Ages = [int[]]::new($this.NewAge+1)
    }

    ImportFish([int[]]$NewFishArray) {
        $NewFishArray| ForEach-Object { $this.Ages[$_]++ }
    }

    [int]SimulateFish([int]$Cycles) {
        for ($C = 0; $C -lt $Cycles; $C++) {
            $NewAges = [int[]]::new($this.NewAge+1)
            for ($A = 0; $A -le $this.NewAge; $A++) {
                switch ($A) {
                    0 {
                        $NewAges[$this.NewAge] += $this.Ages[$A]
                        $NewAges[$this.ResetAge] += $this.Ages[$A]
                    }
                    Default { $NewAges[$A-1] += $this.Ages[$A] }
                }
            }
            $this.Ages = $NewAges
        }
        return ($this.Ages | Measure-Object -Sum).Sum
    }
}

[int[]]$Array = $PuzzleData -split ","
$LanternFishes = [Lanternfish]::new()
$LanternFishes.ImportFish($Array)
$LanternFishes.SimulateFish(80)
