# 00bf9cdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf8ce8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8ce8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0011.md#compare-c7df6a6207b5db779c36c84e678ac0a4)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf9cdc",
  "name": "_ZNSt6__ndk112system_errorC1ENS_10error_codeE",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "230c1816d240347e7d01b2834d9626cfcbf135d74f799808ec652f29542c5f87",
  "source_text_sha256": "230c1816d240347e7d01b2834d9626cfcbf135d74f799808ec652f29542c5f87",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf9cdc",
        "00bf9d6f"
      ]
    ],
    "bytes_sha256": "92d91465591cecfe4cff68613af5180cea8df6a507d8f81d11e84b2eae064ee5",
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

- [00c58f50](../00c58/00c58f50.md)
- [00c5f040](../00c5f/00c5f040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 654 bytes

~~~c

void _ZNSt6__ndk112system_errorC1ENS_10error_codeE(long *param_1,ulong param_2,long *param_3)

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
  _ZNSt13runtime_errorC1ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
            (param_1,local_48);
  if ((local_48[0] & 1) != 0) {
    _ZdlPv(local_38);
  }
  *param_1 = (long)(PTR__ZTVNSt6__ndk112system_errorE_00c9cb70 + 0x10);
  param_1[2] = param_2;
  param_1[3] = (long)param_3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf9cdc"></a> `00bf9cdc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf9ce0"></a> `00bf9ce0` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bf9ce4"></a> `00bf9ce4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf9ce8"></a> `00bf9ce8` | `f5 1b 00 f9` | str x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf9cec"></a> `00bf9cec` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf9cf0"></a> `00bf9cf0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bf9cf4"></a> `00bf9cf4` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00bf9cf8"></a> `00bf9cf8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bf9cfc"></a> `00bf9cfc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bf9d00"></a> `00bf9d00` | `14 01 00 34` | cbz w20,0x00bf9d20 | `CONDITIONAL_JUMP`
<a id="insn-00bf9d04"></a> `00bf9d04` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bf9d08"></a> `00bf9d08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bf9d0c"></a> `00bf9d0c` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00bf9d10"></a> `00bf9d10` | `09 19 40 f9` | ldr x9,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00bf9d14"></a> `00bf9d14` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bf9d18"></a> `00bf9d18` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00bf9d1c"></a> `00bf9d1c` | `03 00 00 14` | b 0x00bf9d28 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf9d20"></a> `00bf9d20` | `ff ff 00 a9` | stp xzr,xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bf9d24"></a> `00bf9d24` | `ff 0f 00 f9` | str xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bf9d28"></a> `00bf9d28` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bf9d2c"></a> `00bf9d2c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bf9d30"></a> `00bf9d30` | `c4 94 01 94` | bl 0x00c5f040 | `UNCONDITIONAL_CALL`
<a id="insn-00bf9d34"></a> `00bf9d34` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bf9d38"></a> `00bf9d38` | `68 00 00 36` | tbz w8,#0x0,0x00bf9d44 | `CONDITIONAL_JUMP`
<a id="insn-00bf9d3c"></a> `00bf9d3c` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bf9d40"></a> `00bf9d40` | `84 7c 01 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bf9d44"></a> `00bf9d44` | `08 05 00 f0` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bf9d48"></a> `00bf9d48` | `08 b9 45 f9` | ldr x8,[x8, #0xb70] | `FALL_THROUGH`
<a id="insn-00bf9d4c"></a> `00bf9d4c` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bf9d50"></a> `00bf9d50` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00bf9d54"></a> `00bf9d54` | `b4 4e 01 a9` | stp x20,x19,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bf9d58"></a> `00bf9d58` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf9d5c"></a> `00bf9d5c` | `f5 1b 40 f9` | ldr x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf9d60"></a> `00bf9d60` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf9d64"></a> `00bf9d64` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bf9d68"></a> `00bf9d68` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf9d6c"></a> `00bf9d6c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf9cdc`](#insn-00bf9cdc) 範囲 `[['00bf9cdc', '00bf9d03']]`
  - `CONDITIONAL_JUMP` [`00bf9d00`](#insn-00bf9d00) → [`00bf9d20`](#insn-00bf9d20)
  - `FALL_THROUGH` [`00bf9d00`](#insn-00bf9d00) → [`00bf9d04`](#insn-00bf9d04)
- ブロック [`00bf9d04`](#insn-00bf9d04) 範囲 `[['00bf9d04', '00bf9d1f']]`
  - `UNCONDITIONAL_JUMP` [`00bf9d1c`](#insn-00bf9d1c) → [`00bf9d28`](#insn-00bf9d28)
- ブロック [`00bf9d20`](#insn-00bf9d20) 範囲 `[['00bf9d20', '00bf9d27']]`
  - `FALL_THROUGH` [`00bf9d24`](#insn-00bf9d24) → [`00bf9d28`](#insn-00bf9d28)
- ブロック [`00bf9d28`](#insn-00bf9d28) 範囲 `[['00bf9d28', '00bf9d3b']]`
  - `CONDITIONAL_JUMP` [`00bf9d38`](#insn-00bf9d38) → [`00bf9d44`](#insn-00bf9d44)
  - `FALL_THROUGH` [`00bf9d38`](#insn-00bf9d38) → [`00bf9d3c`](#insn-00bf9d3c)
- ブロック [`00bf9d3c`](#insn-00bf9d3c) 範囲 `[['00bf9d3c', '00bf9d43']]`
  - `FALL_THROUGH` [`00bf9d40`](#insn-00bf9d40) → [`00bf9d44`](#insn-00bf9d44)
- ブロック [`00bf9d44`](#insn-00bf9d44) 範囲 `[['00bf9d44', '00bf9d6f']]`

## 命令位置別の参照

- [`00bf9ce4`](#insn-00bf9ce4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9ce8`](#insn-00bf9ce8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9cec`](#insn-00bf9cec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9d00`](#insn-00bf9d00) → [`00bf9d20`](#insn-00bf9d20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9d1c`](#insn-00bf9d1c) → [`00bf9d28`](#insn-00bf9d28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9d20`](#insn-00bf9d20) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9d24`](#insn-00bf9d24) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9d30`](#insn-00bf9d30) → [`00c5f040`](../00c5f/00c5f040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f040` · 推定シンボル `None` · 推定型 `None`
- [`00bf9d34`](#insn-00bf9d34) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9d38`](#insn-00bf9d38) → [`00bf9d44`](#insn-00bf9d44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9d3c`](#insn-00bf9d3c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9d40`](#insn-00bf9d40) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bf9d48`](#insn-00bf9d48) → `00c9cb70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bf9d50`](#insn-00bf9d50) → `00c93c10`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`00bf9d58`](#insn-00bf9d58) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9d5c`](#insn-00bf9d5c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9d60`](#insn-00bf9d60) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf9ce4`](#insn-00bf9ce4)

~~~json
{
  "source": "00bf9ce4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9ce8`](#insn-00bf9ce8)

~~~json
{
  "source": "00bf9ce8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9cec`](#insn-00bf9cec)

~~~json
{
  "source": "00bf9cec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9d00`](#insn-00bf9d00)

~~~json
{
  "source": "00bf9d00",
  "target": "00bf9d20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9d1c`](#insn-00bf9d1c)

~~~json
{
  "source": "00bf9d1c",
  "target": "00bf9d28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9d20`](#insn-00bf9d20)

~~~json
{
  "source": "00bf9d20",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9d24`](#insn-00bf9d24)

~~~json
{
  "source": "00bf9d24",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9d30`](#insn-00bf9d30)

~~~json
{
  "source": "00bf9d30",
  "target": "00c5f040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf9d34`](#insn-00bf9d34)

~~~json
{
  "source": "00bf9d34",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9d38`](#insn-00bf9d38)

~~~json
{
  "source": "00bf9d38",
  "target": "00bf9d44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9d3c`](#insn-00bf9d3c)

~~~json
{
  "source": "00bf9d3c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9d40`](#insn-00bf9d40)

~~~json
{
  "source": "00bf9d40",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf9d48`](#insn-00bf9d48)

~~~json
{
  "source": "00bf9d48",
  "target": "00c9cb70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9cb70",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bf9d50`](#insn-00bf9d50)

~~~json
{
  "source": "00bf9d50",
  "target": "00c93c10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93c00",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bf9d58`](#insn-00bf9d58)

~~~json
{
  "source": "00bf9d58",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9d5c`](#insn-00bf9d5c)

~~~json
{
  "source": "00bf9d5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9d60`](#insn-00bf9d60)

~~~json
{
  "source": "00bf9d60",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
