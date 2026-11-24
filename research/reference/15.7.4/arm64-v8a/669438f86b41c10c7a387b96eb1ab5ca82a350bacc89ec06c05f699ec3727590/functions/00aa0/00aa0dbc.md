# 00aa0dbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aa0d78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0d78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0058.md#compare-a69133dfccc56eb73a027cafc9b7fd91)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0088.md#review-d1a3e175dc6c2d9b8d24da1afd4c3412)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa0dbc",
  "name": "FUN_00aa0dbc",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d0f872eb637ea0d2b9630c24aefe505fccdd20e1ca11f889d762f6e72d7159ad",
  "source_text_sha256": "d0f872eb637ea0d2b9630c24aefe505fccdd20e1ca11f889d762f6e72d7159ad",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa0dbc",
        "00aa0e43"
      ]
    ],
    "bytes_sha256": "a4ab8a1a030ebaad6213e4d3ade055329964e5854017784a1153ef7c5fd13161",
    "instruction_count": 34,
    "instruction_bytes": 136,
    "body_bytes": 136,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [009f1ea8](../009f1/009f1ea8.md)
- [009f5650](../009f5/009f5650.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1158 bytes

~~~c

undefined4 FUN_00aa0dbc(int param_1,int param_2,int param_3)

{
  undefined4 *puVar1;
  long lVar2;
  ulong uVar3;
  
                    /* try { // try from 00aa0dbc to 00ba0dcb has its CatchHandler @ 00aa1a40 */
                    /* try { // try from 00aa0dd4 to 00ba0de7 has its CatchHandler @ 00aa1a2c */
  lVar2 = FUN_0081f580();
                    /* try { // try from 00aa0de8 to 00ba0dfb has its CatchHandler @ 00aa1a18 */
  uVar3 = FUN_005c2710(lVar2 + (long)param_1 * 0x1f0 + 0x2678);
  lVar2 = FUN_0081f580();
                    /* try { // try from 00aa0e00 to 00ba0e07 has its CatchHandler @ 00aa1b48 */
                    /* try { // try from 00aa0e10 to 00ba0e1f has its CatchHandler @ 00aa19fc */
                    /* try { // try from 00aa0e28 to 00ba0e3b has its CatchHandler @ 00aa19f8 */
  puVar1 = (undefined4 *)((long)__DT_JMPREL + lVar2 + ((long)param_2 + 2) * 0x1c4 + 0xa448);
  if ((uVar3 & 1) != 0) {
    puVar1 = (undefined4 *)(lVar2 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9ef94);
  }
                    /* try { // try from 00aa0e3c to 00ba0e4f has its CatchHandler @ 00aa19f4 */
  return *puVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa0dbc"></a> `00aa0dbc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aa0dc0"></a> `00aa0dc0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa0dc4"></a> `00aa0dc4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa0dc8"></a> `00aa0dc8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aa0dcc"></a> `00aa0dcc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00aa0dd0"></a> `00aa0dd0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00aa0dd4"></a> `00aa0dd4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aa0dd8"></a> `00aa0dd8` | `ea f9 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0ddc"></a> `00aa0ddc` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00aa0de0"></a> `00aa0de0` | `09 cf 84 52` | mov w9,#0x2678 | `FALL_THROUGH`
<a id="insn-00aa0de4"></a> `00aa0de4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00aa0de8"></a> `00aa0de8` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00aa0dec"></a> `00aa0dec` | `49 86 ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0df0"></a> `00aa0df0` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aa0df4"></a> `00aa0df4` | `e3 f9 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0df8"></a> `00aa0df8` | `88 7e 40 93` | sxtw x8,w20 | `FALL_THROUGH`
<a id="insn-00aa0dfc"></a> `00aa0dfc` | `09 ee 80 52` | mov w9,#0x770 | `FALL_THROUGH`
<a id="insn-00aa0e00"></a> `00aa0e00` | `8a 38 80 52` | mov w10,#0x1c4 | `FALL_THROUGH`
<a id="insn-00aa0e04"></a> `00aa0e04` | `bf 02 00 72` | tst w21,#0x1 | `FALL_THROUGH`
<a id="insn-00aa0e08"></a> `00aa0e08` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00aa0e0c"></a> `00aa0e0c` | `09 01 09 9b` | madd x9,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00aa0e10"></a> `00aa0e10` | `08 01 0a 9b` | madd x8,x8,x10,x0 | `FALL_THROUGH`
<a id="insn-00aa0e14"></a> `00aa0e14` | `8a 3b 80 52` | mov w10,#0x1dc | `FALL_THROUGH`
<a id="insn-00aa0e18"></a> `00aa0e18` | `69 26 2a 9b` | smaddl x9,w19,w10,x9 | `FALL_THROUGH`
<a id="insn-00aa0e1c"></a> `00aa0e1c` | `29 79 42 91` | add x9,x9,#0x9e, LSL #12 | `FALL_THROUGH`
<a id="insn-00aa0e20"></a> `00aa0e20` | `08 e5 48 91` | add x8,x8,#0x239, LSL #12 | `FALL_THROUGH`
<a id="insn-00aa0e24"></a> `00aa0e24` | `29 51 3e 91` | add x9,x9,#0xf94 | `FALL_THROUGH`
<a id="insn-00aa0e28"></a> `00aa0e28` | `08 01 3a 91` | add x8,x8,#0xe80 | `FALL_THROUGH`
<a id="insn-00aa0e2c"></a> `00aa0e2c` | `08 01 89 9a` | csel x8,x8,x9,eq | `FALL_THROUGH`
<a id="insn-00aa0e30"></a> `00aa0e30` | `00 01 40 b9` | ldr w0,[x8] | `FALL_THROUGH`
<a id="insn-00aa0e34"></a> `00aa0e34` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa0e38"></a> `00aa0e38` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa0e3c"></a> `00aa0e3c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aa0e40"></a> `00aa0e40` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa0dbc`](#insn-00aa0dbc) 範囲 `[['00aa0dbc', '00aa0dd3']]`
  - `FALL_THROUGH` [`00aa0dd0`](#insn-00aa0dd0) → [`00aa0dd4`](#insn-00aa0dd4)
- ブロック [`00aa0dd4`](#insn-00aa0dd4) 範囲 `[['00aa0dd4', '00aa0de7']]`
  - `FALL_THROUGH` [`00aa0de4`](#insn-00aa0de4) → [`00aa0de8`](#insn-00aa0de8)
- ブロック [`00aa0de8`](#insn-00aa0de8) 範囲 `[['00aa0de8', '00aa0dff']]`
  - `FALL_THROUGH` [`00aa0dfc`](#insn-00aa0dfc) → [`00aa0e00`](#insn-00aa0e00)
- ブロック [`00aa0e00`](#insn-00aa0e00) 範囲 `[['00aa0e00', '00aa0e0f']]`
  - `FALL_THROUGH` [`00aa0e0c`](#insn-00aa0e0c) → [`00aa0e10`](#insn-00aa0e10)
- ブロック [`00aa0e10`](#insn-00aa0e10) 範囲 `[['00aa0e10', '00aa0e27']]`
  - `FALL_THROUGH` [`00aa0e24`](#insn-00aa0e24) → [`00aa0e28`](#insn-00aa0e28)
- ブロック [`00aa0e28`](#insn-00aa0e28) 範囲 `[['00aa0e28', '00aa0e3b']]`
  - `FALL_THROUGH` [`00aa0e38`](#insn-00aa0e38) → [`00aa0e3c`](#insn-00aa0e3c)
- ブロック [`00aa0e3c`](#insn-00aa0e3c) 範囲 `[['00aa0e3c', '00aa0e43']]`

## 命令位置別の参照

- [`00aa0dbc`](#insn-00aa0dbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0dc0`](#insn-00aa0dc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0dc4`](#insn-00aa0dc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0dd8`](#insn-00aa0dd8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa0dec`](#insn-00aa0dec) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00aa0df4`](#insn-00aa0df4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa0e30`](#insn-00aa0e30) → `00239e80`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1792]`
- [`00aa0e34`](#insn-00aa0e34) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0e38`](#insn-00aa0e38) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0e3c`](#insn-00aa0e3c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa0dbc`](#insn-00aa0dbc)

~~~json
{
  "source": "00aa0dbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0dc0`](#insn-00aa0dc0)

~~~json
{
  "source": "00aa0dc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0dc4`](#insn-00aa0dc4)

~~~json
{
  "source": "00aa0dc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0dd8`](#insn-00aa0dd8)

~~~json
{
  "source": "00aa0dd8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0dec`](#insn-00aa0dec)

~~~json
{
  "source": "00aa0dec",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0df4`](#insn-00aa0df4)

~~~json
{
  "source": "00aa0df4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0e30`](#insn-00aa0e30)

~~~json
{
  "source": "00aa0e30",
  "target": "00239e80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0022fa38",
  "offset": 42056,
  "size": 43008,
  "datatype": "Elf64_Rela[1792]",
  "bytes": "a0c0b1000000000002040000010000000000000000000000a8c0b10000000000",
  "capture_start": "0022fa38",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aa0e34`](#insn-00aa0e34)

~~~json
{
  "source": "00aa0e34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0e38`](#insn-00aa0e38)

~~~json
{
  "source": "00aa0e38",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0e3c`](#insn-00aa0e3c)

~~~json
{
  "source": "00aa0e3c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
