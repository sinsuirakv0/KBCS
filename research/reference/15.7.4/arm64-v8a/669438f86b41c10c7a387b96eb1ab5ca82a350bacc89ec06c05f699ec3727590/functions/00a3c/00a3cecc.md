# 00a3cecc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a3ce88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3ce88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0002.md#compare-cb16e3db8fa6e4bb6b5c1f8daa5bb64f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0079.md#review-1b86e69d5071a3d8aa616499ac461bd5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3cecc",
  "name": "FUN_00a3cecc",
  "size": 196,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3de9573fee8a43d2345f35c2ff5621f1b85cc61b8946fb21906a3ccea7cbf99",
  "source_text_sha256": "e3de9573fee8a43d2345f35c2ff5621f1b85cc61b8946fb21906a3ccea7cbf99",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3cecc",
        "00a3cf8f"
      ]
    ],
    "bytes_sha256": "f6203dd23e3a654753a8bdc7230f4eca04a2e6aa04b45733096b45fc9258fbee",
    "instruction_count": 49,
    "instruction_bytes": 196,
    "body_bytes": 196,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00469e20](../00469/00469e20.md)
- [0046b908](../0046b/0046b908.md)
- [00646dc4](../00646/00646dc4.md)
- [00a02dd4](../00a02/00a02dd4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 948 bytes

~~~c

void FUN_00a3cecc(long param_1,byte *param_2)

{
  byte *pbVar1;
  ulong uVar2;
  long lVar3;
  
  lVar3 = *(long *)(param_1 + 8);
  if ((*param_2 & 1) == 0) {
    *(undefined1 *)(*(long *)(lVar3 + 0x2180) + 0x20) = 0;
  }
  *(undefined1 *)((long)&QWORD_00397074 + lVar3 + 4) = 0;
  FUN_00469e20();
  FUN_0046b908();
  FUN_00646dc4(0xe);
  pbVar1 = BYTE_ARRAY_0032f921 + lVar3 + 0x13;
  pbVar1[0] = 3;
  pbVar1[1] = 0;
  pbVar1[2] = 0;
  pbVar1[3] = 0;
  *(undefined4 *)(&uleb128_0038b164 + lVar3) = 3;
  *(undefined1 *)(lVar3 + 0x32e9) = 1;
  *(undefined4 *)((long)&QWORD_0032e040 + lVar3) = 0;
  uVar2 = FUN_00a02dd4(lVar3 + 0x22b0);
  if ((uVar2 & 1) != 0) {
    *(undefined4 *)((long)&QWORD_0032e040 + lVar3) = 1;
    BYTE_ARRAY_0033322d[lVar3 + 0x17] = 1;
  }
  *(undefined1 *)((long)&DWORD_0032e038 + lVar3) = 1;
  pbVar1 = BYTE_ARRAY_003c3975 + lVar3 + 0x17;
  pbVar1[0] = 0;
  pbVar1[1] = 0;
  pbVar1[2] = 0;
  pbVar1[3] = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a3cecc"></a> `00a3cecc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00a3ced0"></a> `00a3ced0` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3ced4"></a> `00a3ced4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3ced8"></a> `00a3ced8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a3cedc"></a> `00a3cedc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a3cee0"></a> `00a3cee0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a3cee4"></a> `00a3cee4` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a3cee8"></a> `00a3cee8` | `93 31 87 52` | mov w19,#0x398c | `FALL_THROUGH`
<a id="insn-00a3ceec"></a> `00a3ceec` | `29 00 40 39` | ldrb w9,[x1] | `FALL_THROUGH`
<a id="insn-00a3cef0"></a> `00a3cef0` | `08 0f 8e 52` | mov w8,#0x7078 | `FALL_THROUGH`
<a id="insn-00a3cef4"></a> `00a3cef4` | `96 2c 96 52` | mov w22,#0xb164 | `FALL_THROUGH`
<a id="insn-00a3cef8"></a> `00a3cef8` | `97 26 9f 52` | mov w23,#0xf934 | `FALL_THROUGH`
<a id="insn-00a3cefc"></a> `00a3cefc` | `8a ba 4c 91` | add x10,x20,#0x32e, LSL #12 | `FALL_THROUGH`
<a id="insn-00a3cf00"></a> `00a3cf00` | `93 07 a0 72` | movk w19,#0x3c, LSL #16 | `FALL_THROUGH`
<a id="insn-00a3cf04"></a> `00a3cf04` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00a3cf08"></a> `00a3cf08` | `16 07 a0 72` | movk w22,#0x38, LSL #16 | `FALL_THROUGH`
<a id="insn-00a3cf0c"></a> `00a3cf0c` | `57 06 a0 72` | movk w23,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-00a3cf10"></a> `00a3cf10` | `55 e1 00 91` | add x21,x10,#0x38 | `FALL_THROUGH`
<a id="insn-00a3cf14"></a> `00a3cf14` | `38 5d 86 52` | mov w24,#0x32e9 | `FALL_THROUGH`
<a id="insn-00a3cf18"></a> `00a3cf18` | `69 00 00 37` | tbnz w9,#0x0,0x00a3cf24 | `CONDITIONAL_JUMP`
<a id="insn-00a3cf1c"></a> `00a3cf1c` | `89 c2 50 f9` | ldr x9,[x20, #0x2180] | `FALL_THROUGH`
<a id="insn-00a3cf20"></a> `00a3cf20` | `3f 81 00 39` | strb wzr,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00a3cf24"></a> `00a3cf24` | `9f 6a 28 38` | strb wzr,[x20, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00a3cf28"></a> `00a3cf28` | `be b3 e8 97` | bl 0x00469e20 | `UNCONDITIONAL_CALL`
<a id="insn-00a3cf2c"></a> `00a3cf2c` | `77 ba e8 97` | bl 0x0046b908 | `UNCONDITIONAL_CALL`
<a id="insn-00a3cf30"></a> `00a3cf30` | `c0 01 80 52` | mov w0,#0xe | `FALL_THROUGH`
<a id="insn-00a3cf34"></a> `00a3cf34` | `a4 27 f0 97` | bl 0x00646dc4 | `UNCONDITIONAL_CALL`
<a id="insn-00a3cf38"></a> `00a3cf38` | `68 00 80 52` | mov w8,#0x3 | `FALL_THROUGH`
<a id="insn-00a3cf3c"></a> `00a3cf3c` | `88 6a 37 b8` | str w8,[x20, x23, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a3cf40"></a> `00a3cf40` | `39 00 80 52` | mov w25,#0x1 | `FALL_THROUGH`
<a id="insn-00a3cf44"></a> `00a3cf44` | `88 6a 36 b8` | str w8,[x20, x22, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a3cf48"></a> `00a3cf48` | `08 56 84 52` | mov w8,#0x22b0 | `FALL_THROUGH`
<a id="insn-00a3cf4c"></a> `00a3cf4c` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00a3cf50"></a> `00a3cf50` | `99 6a 38 38` | strb w25,[x20, x24, LSL ] | `FALL_THROUGH`
<a id="insn-00a3cf54"></a> `00a3cf54` | `bf 0a 00 b9` | str wzr,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00a3cf58"></a> `00a3cf58` | `9f 17 ff 97` | bl 0x00a02dd4 | `UNCONDITIONAL_CALL`
<a id="insn-00a3cf5c"></a> `00a3cf5c` | `a0 00 00 36` | tbz w0,#0x0,0x00a3cf70 | `CONDITIONAL_JUMP`
<a id="insn-00a3cf60"></a> `00a3cf60` | `88 48 86 52` | mov w8,#0x3244 | `FALL_THROUGH`
<a id="insn-00a3cf64"></a> `00a3cf64` | `b9 0a 00 b9` | str w25,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00a3cf68"></a> `00a3cf68` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00a3cf6c"></a> `00a3cf6c` | `99 6a 28 38` | strb w25,[x20, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00a3cf70"></a> `00a3cf70` | `b9 02 00 39` | strb w25,[x21] | `FALL_THROUGH`
<a id="insn-00a3cf74"></a> `00a3cf74` | `9f 6a 33 b8` | str wzr,[x20, x19, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a3cf78"></a> `00a3cf78` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a3cf7c"></a> `00a3cf7c` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3cf80"></a> `00a3cf80` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a3cf84"></a> `00a3cf84` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3cf88"></a> `00a3cf88` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00a3cf8c"></a> `00a3cf8c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3cecc`](#insn-00a3cecc) 範囲 `[['00a3cecc', '00a3cf1b']]`
  - `CONDITIONAL_JUMP` [`00a3cf18`](#insn-00a3cf18) → [`00a3cf24`](#insn-00a3cf24)
  - `FALL_THROUGH` [`00a3cf18`](#insn-00a3cf18) → [`00a3cf1c`](#insn-00a3cf1c)
- ブロック [`00a3cf1c`](#insn-00a3cf1c) 範囲 `[['00a3cf1c', '00a3cf23']]`
  - `FALL_THROUGH` [`00a3cf20`](#insn-00a3cf20) → [`00a3cf24`](#insn-00a3cf24)
- ブロック [`00a3cf24`](#insn-00a3cf24) 範囲 `[['00a3cf24', '00a3cf5f']]`
  - `CONDITIONAL_JUMP` [`00a3cf5c`](#insn-00a3cf5c) → [`00a3cf70`](#insn-00a3cf70)
  - `FALL_THROUGH` [`00a3cf5c`](#insn-00a3cf5c) → [`00a3cf60`](#insn-00a3cf60)
- ブロック [`00a3cf60`](#insn-00a3cf60) 範囲 `[['00a3cf60', '00a3cf6f']]`
  - `FALL_THROUGH` [`00a3cf6c`](#insn-00a3cf6c) → [`00a3cf70`](#insn-00a3cf70)
- ブロック [`00a3cf70`](#insn-00a3cf70) 範囲 `[['00a3cf70', '00a3cf8f']]`

## 命令位置別の参照

- [`00a3cecc`](#insn-00a3cecc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ced0`](#insn-00a3ced0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ced4`](#insn-00a3ced4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ced8`](#insn-00a3ced8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cedc`](#insn-00a3cedc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cf18`](#insn-00a3cf18) → [`00a3cf24`](#insn-00a3cf24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cf24`](#insn-00a3cf24) → `00397078`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00a3cf28`](#insn-00a3cf28) → [`00469e20`](../00469/00469e20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469e20` · 推定シンボル `None` · 推定型 `None`
- [`00a3cf2c`](#insn-00a3cf2c) → [`0046b908`](../0046b/0046b908.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046b908` · 推定シンボル `None` · 推定型 `None`
- [`00a3cf34`](#insn-00a3cf34) → [`00646dc4`](../00646/00646dc4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00646dc4` · 推定シンボル `None` · 推定型 `None`
- [`00a3cf3c`](#insn-00a3cf3c) → `0032f934`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00a3cf44`](#insn-00a3cf44) → `0038b164`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00a3cf54`](#insn-00a3cf54) → `0032e040`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00a3cf58`](#insn-00a3cf58) → [`00a02dd4`](../00a02/00a02dd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a02dd4` · 推定シンボル `None` · 推定型 `None`
- [`00a3cf5c`](#insn-00a3cf5c) → [`00a3cf70`](#insn-00a3cf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cf64`](#insn-00a3cf64) → `0032e040`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00a3cf6c`](#insn-00a3cf6c) → `00333244`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[27]`
- [`00a3cf70`](#insn-00a3cf70) → `0032e038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00a3cf74`](#insn-00a3cf74) → `003c398c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00a3cf78`](#insn-00a3cf78) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cf7c`](#insn-00a3cf7c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cf80`](#insn-00a3cf80) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cf84`](#insn-00a3cf84) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cf88`](#insn-00a3cf88) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3cecc`](#insn-00a3cecc)

~~~json
{
  "source": "00a3cecc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ced0`](#insn-00a3ced0)

~~~json
{
  "source": "00a3ced0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ced4`](#insn-00a3ced4)

~~~json
{
  "source": "00a3ced4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ced8`](#insn-00a3ced8)

~~~json
{
  "source": "00a3ced8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cedc`](#insn-00a3cedc)

~~~json
{
  "source": "00a3cedc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cf18`](#insn-00a3cf18)

~~~json
{
  "source": "00a3cf18",
  "target": "00a3cf24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cf24`](#insn-00a3cf24)

~~~json
{
  "source": "00a3cf24",
  "target": "00397078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00397074",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "0400000000000000",
  "capture_start": "00397074",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a3cf28`](#insn-00a3cf28)

~~~json
{
  "source": "00a3cf28",
  "target": "00469e20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3cf2c`](#insn-00a3cf2c)

~~~json
{
  "source": "00a3cf2c",
  "target": "0046b908",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3cf34`](#insn-00a3cf34)

~~~json
{
  "source": "00a3cf34",
  "target": "00646dc4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3cf3c`](#insn-00a3cf3c)

~~~json
{
  "source": "00a3cf3c",
  "target": "0032f934",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f921",
  "offset": 19,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d040a640c1f10440e00dedd440b",
  "capture_start": "0032f921",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a3cf44`](#insn-00a3cf44)

~~~json
{
  "source": "00a3cf44",
  "target": "0038b164",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0038b164",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0038b164",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a3cf54`](#insn-00a3cf54)

~~~json
{
  "source": "00a3cf54",
  "target": "0032e040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032e040",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "1c00000000000000",
  "capture_start": "0032e040",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a3cf58`](#insn-00a3cf58)

~~~json
{
  "source": "00a3cf58",
  "target": "00a02dd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3cf5c`](#insn-00a3cf5c)

~~~json
{
  "source": "00a3cf5c",
  "target": "00a3cf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cf64`](#insn-00a3cf64)

~~~json
{
  "source": "00a3cf64",
  "target": "0032e040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032e040",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "1c00000000000000",
  "capture_start": "0032e040",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a3cf6c`](#insn-00a3cf6c)

~~~json
{
  "source": "00a3cf6c",
  "target": "00333244",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033322d",
  "offset": 23,
  "size": 27,
  "datatype": "byte[27]",
  "bytes": "440e20480c1d20930294049e069d08740c1f20480e00d3d4dedd00",
  "capture_start": "0033322d",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a3cf70`](#insn-00a3cf70)

~~~json
{
  "source": "00a3cf70",
  "target": "0032e038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032e038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "402b0000",
  "capture_start": "0032e038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a3cf74`](#insn-00a3cf74)

~~~json
{
  "source": "00a3cf74",
  "target": "003c398c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003c3975",
  "offset": 23,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "442d440e304c0c1d309302940495089e0a9d0c0a02f40c1f304c0e00442dd3d4",
  "capture_start": "003c3975",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00a3cf78`](#insn-00a3cf78)

~~~json
{
  "source": "00a3cf78",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cf7c`](#insn-00a3cf7c)

~~~json
{
  "source": "00a3cf7c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cf80`](#insn-00a3cf80)

~~~json
{
  "source": "00a3cf80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cf84`](#insn-00a3cf84)

~~~json
{
  "source": "00a3cf84",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cf88`](#insn-00a3cf88)

~~~json
{
  "source": "00a3cf88",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
