param([Parameter(Mandatory=$true)][string]$Icon)
$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.Drawing
$workspace=Split-Path -Parent $PSScriptRoot
$destination=Join-Path $workspace 'crates/kbcs-app/assets'
New-Item -ItemType Directory -Force -Path $destination | Out-Null
$source=[System.Drawing.Bitmap]::new((Resolve-Path -LiteralPath $Icon).Path)
$frames=@{}
foreach($size in @(16,32,48,64,128,256,512,1024)){
    $bitmap=[System.Drawing.Bitmap]::new($size,$size)
    $graphics=[System.Drawing.Graphics]::FromImage($bitmap)
    $graphics.InterpolationMode=[System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $graphics.DrawImage($source,0,0,$size,$size)
    $graphics.Dispose()
    $stream=[System.IO.MemoryStream]::new()
    $bitmap.Save($stream,[System.Drawing.Imaging.ImageFormat]::Png)
    $frames[$size]=$stream.ToArray()
    $stream.Dispose()
    if($size -eq 256){
        $rgba=[byte[]]::new($size*$size*4)
        for($y=0;$y -lt $size;$y++){for($x=0;$x -lt $size;$x++){
            $color=$bitmap.GetPixel($x,$y);$at=($y*$size+$x)*4
            $rgba[$at]=$color.R;$rgba[$at+1]=$color.G;$rgba[$at+2]=$color.B;$rgba[$at+3]=$color.A
        }}
        [System.IO.File]::WriteAllBytes((Join-Path $destination 'app-icon.rgba'),$rgba)
    }
    $bitmap.Dispose()
}
$source.Dispose()
# 提供画像の書式とサイズだけを変え、図柄は加工しない。
$stream=[System.IO.MemoryStream]::new();$writer=[System.IO.BinaryWriter]::new($stream)
$sizes=@(16,32,48,64,128,256)
$writer.Write([uint16]0);$writer.Write([uint16]1);$writer.Write([uint16]$sizes.Count)
$offset=6+16*$sizes.Count
foreach($size in $sizes){
    $dimension=if($size -eq 256){0}else{$size}
    $writer.Write([byte]$dimension);$writer.Write([byte]$dimension);$writer.Write([uint16]0)
    $writer.Write([uint16]1);$writer.Write([uint16]32);$writer.Write([uint32]$frames[$size].Length);$writer.Write([uint32]$offset)
    $offset+=$frames[$size].Length
}
foreach($size in $sizes){$writer.Write([byte[]]$frames[$size])}
[System.IO.File]::WriteAllBytes((Join-Path $destination 'app.ico'),$stream.ToArray())
$writer.Dispose();$stream.Dispose()
$stream=[System.IO.MemoryStream]::new();$writer=[System.IO.BinaryWriter]::new($stream)
$types=@{128='ic07';256='ic08';512='ic09';1024='ic10'}
$length=8;foreach($size in $types.Keys){$length+=8+$frames[$size].Length}
$writer.Write([System.Text.Encoding]::ASCII.GetBytes('icns'))
$writer.Write([byte[]]([BitConverter]::GetBytes([int32]$length)[3..0]))
foreach($size in @(128,256,512,1024)){
    $writer.Write([System.Text.Encoding]::ASCII.GetBytes($types[$size]))
    $writer.Write([byte[]]([BitConverter]::GetBytes([int32](8+$frames[$size].Length))[3..0]))
    $writer.Write([byte[]]$frames[$size])
}
[System.IO.File]::WriteAllBytes((Join-Path $destination 'app.icns'),$stream.ToArray())
$writer.Dispose();$stream.Dispose()
