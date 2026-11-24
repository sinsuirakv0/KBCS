# 00ac2fcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0161.md#review-e9d67d5fc573362ca34220e3f5167ad4)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0042.md#review-e9d67d5fc573362ca34220e3f5167ad4)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac2fcc",
  "name": "FUN_00ac2fcc",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "96fd3067ed80ab2c33226bb442bdfca2b8b6b367e4bec66491b56c721d7919b8",
  "source_text_sha256": "96fd3067ed80ab2c33226bb442bdfca2b8b6b367e4bec66491b56c721d7919b8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ac2fcc",
        "00ac303f"
      ]
    ],
    "bytes_sha256": "cc767fe7acc731afc50fceb9002ea22e31c007a1dcae92f3cd624042920ba369",
    "instruction_count": 29,
    "instruction_bytes": 116,
    "body_bytes": 116,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [008b79cc](../008b7/008b79cc.md)
- [00abf2b4](../00abf/00abf2b4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 552 bytes

~~~c

void FUN_00ac2fcc(long param_1)

{
  long lVar1;
  
  lVar1 = *(long *)(param_1 + 8);
  FUN_00abf2b4(param_1,1);
  if ((*(byte *)(lVar1 + 0x1aec) & 1) != 0) {
                    /* try { // try from 00ac2ff8 to 00bc2ffb has its CatchHandler @ 00ac3114 */
                    /* try { // try from 00ac2ffc to 00bc30b3 has its CatchHandler @ 00ac2c48 */
    return;
  }
  *(undefined1 *)(lVar1 + 0x1aec) = 1;
  *(undefined4 *)((long)&QWORD_0039b1b4 + lVar1) = 2;
  *(undefined4 *)(lVar1 + 0x3478) = 0x22;
  FUN_008b79cc(lVar1 + 0x2f38,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ac2fcc"></a> `00ac2fcc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00ac2fd0"></a> `00ac2fd0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ac2fd4"></a> `00ac2fd4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac2fd8"></a> `00ac2fd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ac2fdc"></a> `00ac2fdc` | `13 04 40 f9` | ldr x19,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00ac2fe0"></a> `00ac2fe0` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00ac2fe4"></a> `00ac2fe4` | `94 5d 83 52` | mov w20,#0x1aec | `FALL_THROUGH`
<a id="insn-00ac2fe8"></a> `00ac2fe8` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-00ac2fec"></a> `00ac2fec` | `b2 f0 ff 97` | bl 0x00abf2b4 | `UNCONDITIONAL_CALL`
<a id="insn-00ac2ff0"></a> `00ac2ff0` | `68 6a 74 38` | ldrb w8,[x19, x20, LSL ] | `FALL_THROUGH`
<a id="insn-00ac2ff4"></a> `00ac2ff4` | `a8 00 00 36` | tbz w8,#0x0,0x00ac3008 | `CONDITIONAL_JUMP`
<a id="insn-00ac2ff8"></a> `00ac2ff8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac2ffc"></a> `00ac2ffc` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ac3000"></a> `00ac3000` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00ac3004"></a> `00ac3004` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ac3008"></a> `00ac3008` | `88 36 96 52` | mov w8,#0xb1b4 | `FALL_THROUGH`
<a id="insn-00ac300c"></a> `00ac300c` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00ac3010"></a> `00ac3010` | `0a e7 85 52` | mov w10,#0x2f38 | `FALL_THROUGH`
<a id="insn-00ac3014"></a> `00ac3014` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00ac3018"></a> `00ac3018` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00ac301c"></a> `00ac301c` | `75 6a 34 38` | strb w21,[x19, x20, LSL ] | `FALL_THROUGH`
<a id="insn-00ac3020"></a> `00ac3020` | `69 6a 28 b8` | str w9,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac3024"></a> `00ac3024` | `48 04 80 52` | mov w8,#0x22 | `FALL_THROUGH`
<a id="insn-00ac3028"></a> `00ac3028` | `60 02 0a 8b` | add x0,x19,x10 | `FALL_THROUGH`
<a id="insn-00ac302c"></a> `00ac302c` | `68 7a 34 b9` | str w8,[x19, #0x3478] | `FALL_THROUGH`
<a id="insn-00ac3030"></a> `00ac3030` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac3034"></a> `00ac3034` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ac3038"></a> `00ac3038` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00ac303c"></a> `00ac303c` | `64 d2 f7 17` | b 0x008b79cc | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ac2fcc`](#insn-00ac2fcc) 範囲 `[['00ac2fcc', '00ac2ff7']]`
  - `CONDITIONAL_JUMP` [`00ac2ff4`](#insn-00ac2ff4) → [`00ac3008`](#insn-00ac3008)
  - `FALL_THROUGH` [`00ac2ff4`](#insn-00ac2ff4) → [`00ac2ff8`](#insn-00ac2ff8)
- ブロック [`00ac2ff8`](#insn-00ac2ff8) 範囲 `[['00ac2ff8', '00ac2ffb']]`
  - `FALL_THROUGH` [`00ac2ff8`](#insn-00ac2ff8) → [`00ac2ffc`](#insn-00ac2ffc)
- ブロック [`00ac2ffc`](#insn-00ac2ffc) 範囲 `[['00ac2ffc', '00ac3007']]`
- ブロック [`00ac3008`](#insn-00ac3008) 範囲 `[['00ac3008', '00ac303f']]`

## 命令位置別の参照

- [`00ac2fcc`](#insn-00ac2fcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2fd0`](#insn-00ac2fd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2fd4`](#insn-00ac2fd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2fec`](#insn-00ac2fec) → [`00abf2b4`](../00abf/00abf2b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00abf2b4` · 推定シンボル `None` · 推定型 `None`
- [`00ac2ff4`](#insn-00ac2ff4) → [`00ac3008`](#insn-00ac3008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2ff8`](#insn-00ac2ff8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2ffc`](#insn-00ac2ffc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac3000`](#insn-00ac3000) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac3020`](#insn-00ac3020) → `0039b1b4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ac3030`](#insn-00ac3030) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac3034`](#insn-00ac3034) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac3038`](#insn-00ac3038) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac303c`](#insn-00ac303c) → [`008b79cc`](../008b7/008b79cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b79cc` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ac2fcc`](#insn-00ac2fcc)

~~~json
{
  "source": "00ac2fcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2fd0`](#insn-00ac2fd0)

~~~json
{
  "source": "00ac2fd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2fd4`](#insn-00ac2fd4)

~~~json
{
  "source": "00ac2fd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2fec`](#insn-00ac2fec)

~~~json
{
  "source": "00ac2fec",
  "target": "00abf2b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac2ff4`](#insn-00ac2ff4)

~~~json
{
  "source": "00ac2ff4",
  "target": "00ac3008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2ff8`](#insn-00ac2ff8)

~~~json
{
  "source": "00ac2ff8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2ffc`](#insn-00ac2ffc)

~~~json
{
  "source": "00ac2ffc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac3000`](#insn-00ac3000)

~~~json
{
  "source": "00ac3000",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac3020`](#insn-00ac3020)

~~~json
{
  "source": "00ac3020",
  "target": "0039b1b4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b1b4",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "0c00000000000000",
  "capture_start": "0039b1b4",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ac3030`](#insn-00ac3030)

~~~json
{
  "source": "00ac3030",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac3034`](#insn-00ac3034)

~~~json
{
  "source": "00ac3034",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac3038`](#insn-00ac3038)

~~~json
{
  "source": "00ac3038",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac303c`](#insn-00ac303c)

~~~json
{
  "source": "00ac303c",
  "target": "008b79cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
