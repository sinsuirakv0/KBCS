# 00b7bddc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b7bd98`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7bd98.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0011.md#compare-6fbc29e8cfeb155d88144c3b5f0c2b42)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bf8824`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8824.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-c9c6ce9ce5798ca8f5484739d3e93e7f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7bddc",
  "name": "_ZNSt6__ndk112system_errorC2ENS_10error_codeE",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "21f2dc4629a6fc31c406200a315a88c3ee7db217a55f1e008c422237bd508c42",
  "source_text_sha256": "21f2dc4629a6fc31c406200a315a88c3ee7db217a55f1e008c422237bd508c42",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7bddc",
        "00b7be6f"
      ]
    ],
    "bytes_sha256": "ff76c4d5d049d4054a2af3f1b54e8a48db819bbaeaff582e854565996ca98393",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00be0fa0](../00be0/00be0fa0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 654 bytes

~~~c

void _ZNSt6__ndk112system_errorC2ENS_10error_codeE(long *param_1,ulong param_2,long *param_3)

{
  ulong local_48 [2];
  void *local_38;
  
  if ((int)param_2 == 0) {
    local_48[0] = 0;
    local_48[1] = 0;
    local_38 = (void *)0x0;
  }
  else {
    (**(code **)(*param_3 + 0x30))(local_48,param_3,param_2 & 0xffffffff);
  }
  _ZNSt13runtime_errorC2ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
            (param_1,local_48);
  if ((local_48[0] & 1) != 0) {
    _ZdlPv(local_38);
  }
  *param_1 = (long)(PTR__ZTVNSt6__ndk112system_errorE_00c1bca0 + 0x10);
  param_1[2] = param_2;
  param_1[3] = (long)param_3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b7bddc"></a> `00b7bddc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00b7bde0"></a> `00b7bde0` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b7bde4"></a> `00b7bde4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b7bde8"></a> `00b7bde8` | `f5 1b 00 f9` | str x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b7bdec"></a> `00b7bdec` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b7bdf0"></a> `00b7bdf0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b7bdf4"></a> `00b7bdf4` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00b7bdf8"></a> `00b7bdf8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00b7bdfc"></a> `00b7bdfc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b7be00"></a> `00b7be00` | `14 01 00 34` | cbz w20,0x00b7be20 | `CONDITIONAL_JUMP`
<a id="insn-00b7be04"></a> `00b7be04` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b7be08"></a> `00b7be08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b7be0c"></a> `00b7be0c` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00b7be10"></a> `00b7be10` | `09 19 40 f9` | ldr x9,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00b7be14"></a> `00b7be14` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b7be18"></a> `00b7be18` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00b7be1c"></a> `00b7be1c` | `03 00 00 14` | b 0x00b7be28 | `UNCONDITIONAL_JUMP`
<a id="insn-00b7be20"></a> `00b7be20` | `ff ff 00 a9` | stp xzr,xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b7be24"></a> `00b7be24` | `ff 0f 00 f9` | str xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b7be28"></a> `00b7be28` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b7be2c"></a> `00b7be2c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b7be30"></a> `00b7be30` | `5c 94 01 94` | bl 0x00be0fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00b7be34"></a> `00b7be34` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b7be38"></a> `00b7be38` | `68 00 00 36` | tbz w8,#0x0,0x00b7be44 | `CONDITIONAL_JUMP`
<a id="insn-00b7be3c"></a> `00b7be3c` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b7be40"></a> `00b7be40` | `88 7c 01 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b7be44"></a> `00b7be44` | `08 05 00 90` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00b7be48"></a> `00b7be48` | `08 51 46 f9` | ldr x8,[x8, #0xca0] | `FALL_THROUGH`
<a id="insn-00b7be4c"></a> `00b7be4c` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00b7be50"></a> `00b7be50` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00b7be54"></a> `00b7be54` | `b4 4e 01 a9` | stp x20,x19,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00b7be58"></a> `00b7be58` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b7be5c"></a> `00b7be5c` | `f5 1b 40 f9` | ldr x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b7be60"></a> `00b7be60` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b7be64"></a> `00b7be64` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b7be68"></a> `00b7be68` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00b7be6c"></a> `00b7be6c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b7bddc`](#insn-00b7bddc) 範囲 `[['00b7bddc', '00b7be03']]`
  - `CONDITIONAL_JUMP` [`00b7be00`](#insn-00b7be00) → [`00b7be20`](#insn-00b7be20)
  - `FALL_THROUGH` [`00b7be00`](#insn-00b7be00) → [`00b7be04`](#insn-00b7be04)
- ブロック [`00b7be04`](#insn-00b7be04) 範囲 `[['00b7be04', '00b7be1f']]`
  - `UNCONDITIONAL_JUMP` [`00b7be1c`](#insn-00b7be1c) → [`00b7be28`](#insn-00b7be28)
- ブロック [`00b7be20`](#insn-00b7be20) 範囲 `[['00b7be20', '00b7be27']]`
  - `FALL_THROUGH` [`00b7be24`](#insn-00b7be24) → [`00b7be28`](#insn-00b7be28)
- ブロック [`00b7be28`](#insn-00b7be28) 範囲 `[['00b7be28', '00b7be3b']]`
  - `CONDITIONAL_JUMP` [`00b7be38`](#insn-00b7be38) → [`00b7be44`](#insn-00b7be44)
  - `FALL_THROUGH` [`00b7be38`](#insn-00b7be38) → [`00b7be3c`](#insn-00b7be3c)
- ブロック [`00b7be3c`](#insn-00b7be3c) 範囲 `[['00b7be3c', '00b7be43']]`
  - `FALL_THROUGH` [`00b7be40`](#insn-00b7be40) → [`00b7be44`](#insn-00b7be44)
- ブロック [`00b7be44`](#insn-00b7be44) 範囲 `[['00b7be44', '00b7be6f']]`

## 命令位置別の参照

- [`00b7bde4`](#insn-00b7bde4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7bde8`](#insn-00b7bde8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7bdec`](#insn-00b7bdec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7be00`](#insn-00b7be00) → [`00b7be20`](#insn-00b7be20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7be1c`](#insn-00b7be1c) → [`00b7be28`](#insn-00b7be28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7be20`](#insn-00b7be20) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7be24`](#insn-00b7be24) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7be30`](#insn-00b7be30) → [`00be0fa0`](../00be0/00be0fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0fa0` · 推定シンボル `None` · 推定型 `None`
- [`00b7be34`](#insn-00b7be34) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7be38`](#insn-00b7be38) → [`00b7be44`](#insn-00b7be44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7be3c`](#insn-00b7be3c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7be40`](#insn-00b7be40) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b7be48`](#insn-00b7be48) → `00c1bca0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b7be50`](#insn-00b7be50) → `00c12dc8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`00b7be58`](#insn-00b7be58) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7be5c`](#insn-00b7be5c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7be60`](#insn-00b7be60) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7bde4`](#insn-00b7bde4)

~~~json
{
  "source": "00b7bde4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7bde8`](#insn-00b7bde8)

~~~json
{
  "source": "00b7bde8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7bdec`](#insn-00b7bdec)

~~~json
{
  "source": "00b7bdec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7be00`](#insn-00b7be00)

~~~json
{
  "source": "00b7be00",
  "target": "00b7be20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7be1c`](#insn-00b7be1c)

~~~json
{
  "source": "00b7be1c",
  "target": "00b7be28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7be20`](#insn-00b7be20)

~~~json
{
  "source": "00b7be20",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7be24`](#insn-00b7be24)

~~~json
{
  "source": "00b7be24",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7be30`](#insn-00b7be30)

~~~json
{
  "source": "00b7be30",
  "target": "00be0fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7be34`](#insn-00b7be34)

~~~json
{
  "source": "00b7be34",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7be38`](#insn-00b7be38)

~~~json
{
  "source": "00b7be38",
  "target": "00b7be44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7be3c`](#insn-00b7be3c)

~~~json
{
  "source": "00b7be3c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7be40`](#insn-00b7be40)

~~~json
{
  "source": "00b7be40",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7be48`](#insn-00b7be48)

~~~json
{
  "source": "00b7be48",
  "target": "00c1bca0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bca0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b7be50`](#insn-00b7be50)

~~~json
{
  "source": "00b7be50",
  "target": "00c12dc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c12db8",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00b7be58`](#insn-00b7be58)

~~~json
{
  "source": "00b7be58",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7be5c`](#insn-00b7be5c)

~~~json
{
  "source": "00b7be5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7be60`](#insn-00b7be60)

~~~json
{
  "source": "00b7be60",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
