# 00aa2ffc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aa2fb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2fb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0006.md#compare-005a4ca91aa2ba92b3e8be070fe44a19)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0088.md#review-0fad6723dbe1ea87077350764af85976)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa2ffc",
  "name": "FUN_00aa2ffc",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2c0ba816b0813260d7ea3d37dac4a70191d02f27c27fe9ba201f85dad16528b4",
  "source_text_sha256": "2c0ba816b0813260d7ea3d37dac4a70191d02f27c27fe9ba201f85dad16528b4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa2ffc",
        "00aa3073"
      ]
    ],
    "bytes_sha256": "fb5eabad17dcdc2df36f33f9ff125ec72e8dd36599f4eb029b96797820b67da3",
    "instruction_count": 30,
    "instruction_bytes": 120,
    "body_bytes": 120,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006a0ab4](../006a0/006a0ab4.md)
- [009f1ea8](../009f1/009f1ea8.md)
- [00aa0f64](../00aa0/00aa0f64.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 396 bytes

~~~c

bool FUN_00aa2ffc(int param_1,int param_2,int param_3)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_0081f580();
  uVar3 = FUN_005c2710(lVar2 + (long)param_1 * 0x1f0 + 0x2678);
  if ((uVar3 & 1) == 0) {
    bVar1 = false;
  }
  else {
    lVar2 = FUN_0081f580();
    bVar1 = *(int *)(lVar2 + (long)param_2 * 0x770 + (long)param_3 * 0x1dc + 0x9feac) != 0;
  }
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa2ffc"></a> `00aa2ffc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aa3000"></a> `00aa3000` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa3004"></a> `00aa3004` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa3008"></a> `00aa3008` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aa300c"></a> `00aa300c` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00aa3010"></a> `00aa3010` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00aa3014"></a> `00aa3014` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aa3018"></a> `00aa3018` | `5a f1 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa301c"></a> `00aa301c` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00aa3020"></a> `00aa3020` | `09 cf 84 52` | mov w9,#0x2678 | `FALL_THROUGH`
<a id="insn-00aa3024"></a> `00aa3024` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00aa3028"></a> `00aa3028` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00aa302c"></a> `00aa302c` | `b9 7d ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00aa3030"></a> `00aa3030` | `60 00 00 37` | tbnz w0,#0x0,0x00aa303c | `CONDITIONAL_JUMP`
<a id="insn-00aa3034"></a> `00aa3034` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aa3038"></a> `00aa3038` | `0b 00 00 14` | b 0x00aa3064 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa303c"></a> `00aa303c` | `51 f1 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa3040"></a> `00aa3040` | `08 ee 80 52` | mov w8,#0x770 | `FALL_THROUGH`
<a id="insn-00aa3044"></a> `00aa3044` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00aa3048"></a> `00aa3048` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00aa304c"></a> `00aa304c` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00aa3050"></a> `00aa3050` | `89 d5 9f 52` | mov w9,#0xfeac | `FALL_THROUGH`
<a id="insn-00aa3054"></a> `00aa3054` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa3058"></a> `00aa3058` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa305c"></a> `00aa305c` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00aa3060"></a> `00aa3060` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00aa3064"></a> `00aa3064` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa3068"></a> `00aa3068` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa306c"></a> `00aa306c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aa3070"></a> `00aa3070` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa2ffc`](#insn-00aa2ffc) 範囲 `[['00aa2ffc', '00aa3033']]`
  - `CONDITIONAL_JUMP` [`00aa3030`](#insn-00aa3030) → [`00aa303c`](#insn-00aa303c)
  - `FALL_THROUGH` [`00aa3030`](#insn-00aa3030) → [`00aa3034`](#insn-00aa3034)
- ブロック [`00aa3034`](#insn-00aa3034) 範囲 `[['00aa3034', '00aa303b']]`
  - `UNCONDITIONAL_JUMP` [`00aa3038`](#insn-00aa3038) → [`00aa3064`](#insn-00aa3064)
- ブロック [`00aa303c`](#insn-00aa303c) 範囲 `[['00aa303c', '00aa3063']]`
  - `FALL_THROUGH` [`00aa3060`](#insn-00aa3060) → [`00aa3064`](#insn-00aa3064)
- ブロック [`00aa3064`](#insn-00aa3064) 範囲 `[['00aa3064', '00aa3073']]`

## 命令位置別の参照

- [`00aa2ffc`](#insn-00aa2ffc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3000`](#insn-00aa3000) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3004`](#insn-00aa3004) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3018`](#insn-00aa3018) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa302c`](#insn-00aa302c) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00aa3030`](#insn-00aa3030) → [`00aa303c`](#insn-00aa303c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3038`](#insn-00aa3038) → [`00aa3064`](#insn-00aa3064) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa303c`](#insn-00aa303c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa3064`](#insn-00aa3064) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3068`](#insn-00aa3068) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa306c`](#insn-00aa306c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa2ffc`](#insn-00aa2ffc)

~~~json
{
  "source": "00aa2ffc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3000`](#insn-00aa3000)

~~~json
{
  "source": "00aa3000",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3004`](#insn-00aa3004)

~~~json
{
  "source": "00aa3004",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3018`](#insn-00aa3018)

~~~json
{
  "source": "00aa3018",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa302c`](#insn-00aa302c)

~~~json
{
  "source": "00aa302c",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa3030`](#insn-00aa3030)

~~~json
{
  "source": "00aa3030",
  "target": "00aa303c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3038`](#insn-00aa3038)

~~~json
{
  "source": "00aa3038",
  "target": "00aa3064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa303c`](#insn-00aa303c)

~~~json
{
  "source": "00aa303c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa3064`](#insn-00aa3064)

~~~json
{
  "source": "00aa3064",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3068`](#insn-00aa3068)

~~~json
{
  "source": "00aa3068",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa306c`](#insn-00aa306c)

~~~json
{
  "source": "00aa306c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
