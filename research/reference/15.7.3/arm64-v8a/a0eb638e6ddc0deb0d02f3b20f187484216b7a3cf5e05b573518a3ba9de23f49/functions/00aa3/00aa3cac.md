# 00aa3cac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aa3cac`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa3/00aa3cac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0025.md#compare-55348e70423a42f7b1a1b3b89be38b17)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aa3cf0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa3cf0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0058.md#compare-b0e6c26dad7961f889b7aa1add0f749b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa3cac",
  "name": "FUN_00aa3cac",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8f365afc45f9c337870f4ffbf799b40dcccd9f26554705ba5819e08785d1d432",
  "source_text_sha256": "8f365afc45f9c337870f4ffbf799b40dcccd9f26554705ba5819e08785d1d432",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa3cac",
        "00aa3d3f"
      ]
    ],
    "bytes_sha256": "01fce3a8671bf92ee775076ed35b6eae4a9af335c2369e42f9a06ebd71136d24",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006a0ab4](../006a0/006a0ab4.md)
- [006a4d58](../006a4/006a4d58.md)
- [009f1e64](../009f1/009f1e64.md)
- [00aa0f20](../00aa0/00aa0f20.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)
- [00aa2c2c](../00aa2/00aa2c2c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 887 bytes

~~~c

undefined8 FUN_00aa3cac(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  undefined8 uVar3;
  
                    /* try { // try from 00aa3cc8 to 00ba3cd7 has its CatchHandler @ 00aa5998 */
  lVar1 = FUN_0081f580();
                    /* try { // try from 00aa3cd8 to 00ba3ceb has its CatchHandler @ 00aa5970 */
  uVar2 = FUN_005c2710(lVar1 + (long)param_1 * 0x1f0 + 0x2678);
  if ((uVar2 & 1) == 0) {
    uVar3 = 0;
  }
  else {
    lVar1 = FUN_0081f580();
    if (*(int *)(lVar1 + (long)param_2 * 0x770 + (long)param_3 * 0x1dc + 0x9feec) == 0) {
      uVar3 = FUN_00aa2c2c(lVar1,param_2,param_3,0x3f);
      return uVar3;
    }
    uVar3 = 1;
  }
                    /* try { // try from 00aa3d18 to 00ba3d1f has its CatchHandler @ 00aa5a58 */
                    /* try { // try from 00aa3d20 to 00ba3d5b has its CatchHandler @ 00aa5a70 */
  return uVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa3cac"></a> `00aa3cac` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aa3cb0"></a> `00aa3cb0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa3cb4"></a> `00aa3cb4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa3cb8"></a> `00aa3cb8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aa3cbc"></a> `00aa3cbc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00aa3cc0"></a> `00aa3cc0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00aa3cc4"></a> `00aa3cc4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aa3cc8"></a> `00aa3cc8` | `2e ee f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa3ccc"></a> `00aa3ccc` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00aa3cd0"></a> `00aa3cd0` | `09 cf 84 52` | mov w9,#0x2678 | `FALL_THROUGH`
<a id="insn-00aa3cd4"></a> `00aa3cd4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00aa3cd8"></a> `00aa3cd8` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00aa3cdc"></a> `00aa3cdc` | `8d 7a ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00aa3ce0"></a> `00aa3ce0` | `60 00 00 37` | tbnz w0,#0x0,0x00aa3cec | `CONDITIONAL_JUMP`
<a id="insn-00aa3ce4"></a> `00aa3ce4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aa3ce8"></a> `00aa3ce8` | `0b 00 00 14` | b 0x00aa3d14 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa3cec"></a> `00aa3cec` | `25 ee f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa3cf0"></a> `00aa3cf0` | `08 ee 80 52` | mov w8,#0x770 | `FALL_THROUGH`
<a id="insn-00aa3cf4"></a> `00aa3cf4` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00aa3cf8"></a> `00aa3cf8` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00aa3cfc"></a> `00aa3cfc` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00aa3d00"></a> `00aa3d00` | `89 dd 9f 52` | mov w9,#0xfeec | `FALL_THROUGH`
<a id="insn-00aa3d04"></a> `00aa3d04` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa3d08"></a> `00aa3d08` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa3d0c"></a> `00aa3d0c` | `c8 00 00 34` | cbz w8,0x00aa3d24 | `CONDITIONAL_JUMP`
<a id="insn-00aa3d10"></a> `00aa3d10` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aa3d14"></a> `00aa3d14` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa3d18"></a> `00aa3d18` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa3d1c"></a> `00aa3d1c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aa3d20"></a> `00aa3d20` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aa3d24"></a> `00aa3d24` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00aa3d28"></a> `00aa3d28` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00aa3d2c"></a> `00aa3d2c` | `e3 07 80 52` | mov w3,#0x3f | `FALL_THROUGH`
<a id="insn-00aa3d30"></a> `00aa3d30` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa3d34"></a> `00aa3d34` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa3d38"></a> `00aa3d38` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aa3d3c"></a> `00aa3d3c` | `bc fb ff 17` | b 0x00aa2c2c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa3cac`](#insn-00aa3cac) 範囲 `[['00aa3cac', '00aa3cc7']]`
  - `FALL_THROUGH` [`00aa3cc4`](#insn-00aa3cc4) → [`00aa3cc8`](#insn-00aa3cc8)
- ブロック [`00aa3cc8`](#insn-00aa3cc8) 範囲 `[['00aa3cc8', '00aa3cd7']]`
  - `FALL_THROUGH` [`00aa3cd4`](#insn-00aa3cd4) → [`00aa3cd8`](#insn-00aa3cd8)
- ブロック [`00aa3cd8`](#insn-00aa3cd8) 範囲 `[['00aa3cd8', '00aa3ce3']]`
  - `CONDITIONAL_JUMP` [`00aa3ce0`](#insn-00aa3ce0) → [`00aa3cec`](#insn-00aa3cec)
  - `FALL_THROUGH` [`00aa3ce0`](#insn-00aa3ce0) → [`00aa3ce4`](#insn-00aa3ce4)
- ブロック [`00aa3ce4`](#insn-00aa3ce4) 範囲 `[['00aa3ce4', '00aa3ceb']]`
  - `UNCONDITIONAL_JUMP` [`00aa3ce8`](#insn-00aa3ce8) → [`00aa3d14`](#insn-00aa3d14)
- ブロック [`00aa3cec`](#insn-00aa3cec) 範囲 `[['00aa3cec', '00aa3d0f']]`
  - `CONDITIONAL_JUMP` [`00aa3d0c`](#insn-00aa3d0c) → [`00aa3d24`](#insn-00aa3d24)
  - `FALL_THROUGH` [`00aa3d0c`](#insn-00aa3d0c) → [`00aa3d10`](#insn-00aa3d10)
- ブロック [`00aa3d10`](#insn-00aa3d10) 範囲 `[['00aa3d10', '00aa3d13']]`
  - `FALL_THROUGH` [`00aa3d10`](#insn-00aa3d10) → [`00aa3d14`](#insn-00aa3d14)
- ブロック [`00aa3d14`](#insn-00aa3d14) 範囲 `[['00aa3d14', '00aa3d17']]`
  - `FALL_THROUGH` [`00aa3d14`](#insn-00aa3d14) → [`00aa3d18`](#insn-00aa3d18)
- ブロック [`00aa3d18`](#insn-00aa3d18) 範囲 `[['00aa3d18', '00aa3d1f']]`
  - `FALL_THROUGH` [`00aa3d1c`](#insn-00aa3d1c) → [`00aa3d20`](#insn-00aa3d20)
- ブロック [`00aa3d20`](#insn-00aa3d20) 範囲 `[['00aa3d20', '00aa3d23']]`
- ブロック [`00aa3d24`](#insn-00aa3d24) 範囲 `[['00aa3d24', '00aa3d3f']]`

## 命令位置別の参照

- [`00aa3cac`](#insn-00aa3cac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3cb0`](#insn-00aa3cb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3cb4`](#insn-00aa3cb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3cc8`](#insn-00aa3cc8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa3cdc`](#insn-00aa3cdc) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00aa3ce0`](#insn-00aa3ce0) → [`00aa3cec`](#insn-00aa3cec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3ce8`](#insn-00aa3ce8) → [`00aa3d14`](#insn-00aa3d14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3cec`](#insn-00aa3cec) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa3d0c`](#insn-00aa3d0c) → [`00aa3d24`](#insn-00aa3d24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3d14`](#insn-00aa3d14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3d18`](#insn-00aa3d18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3d1c`](#insn-00aa3d1c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3d30`](#insn-00aa3d30) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3d34`](#insn-00aa3d34) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3d38`](#insn-00aa3d38) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3d3c`](#insn-00aa3d3c) → [`00aa2c2c`](../00aa2/00aa2c2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aa2c2c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa3cac`](#insn-00aa3cac)

~~~json
{
  "source": "00aa3cac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3cb0`](#insn-00aa3cb0)

~~~json
{
  "source": "00aa3cb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3cb4`](#insn-00aa3cb4)

~~~json
{
  "source": "00aa3cb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3cc8`](#insn-00aa3cc8)

~~~json
{
  "source": "00aa3cc8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa3cdc`](#insn-00aa3cdc)

~~~json
{
  "source": "00aa3cdc",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa3ce0`](#insn-00aa3ce0)

~~~json
{
  "source": "00aa3ce0",
  "target": "00aa3cec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3ce8`](#insn-00aa3ce8)

~~~json
{
  "source": "00aa3ce8",
  "target": "00aa3d14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3cec`](#insn-00aa3cec)

~~~json
{
  "source": "00aa3cec",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa3d0c`](#insn-00aa3d0c)

~~~json
{
  "source": "00aa3d0c",
  "target": "00aa3d24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3d14`](#insn-00aa3d14)

~~~json
{
  "source": "00aa3d14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3d18`](#insn-00aa3d18)

~~~json
{
  "source": "00aa3d18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3d1c`](#insn-00aa3d1c)

~~~json
{
  "source": "00aa3d1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3d30`](#insn-00aa3d30)

~~~json
{
  "source": "00aa3d30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3d34`](#insn-00aa3d34)

~~~json
{
  "source": "00aa3d34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3d38`](#insn-00aa3d38)

~~~json
{
  "source": "00aa3d38",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3d3c`](#insn-00aa3d3c)

~~~json
{
  "source": "00aa3d3c",
  "target": "00aa2c2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
