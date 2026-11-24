# 00bfe0ac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfd0b8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfd0b8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0087.md#compare-03b22bfdb031253c9957ca13335dc331)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfe0ac",
  "name": "FUN_00bfe0ac",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1bad72b0db980f7b283f029f7a06996ca454dadd2f7dd033bfbf3c0c004da162",
  "source_text_sha256": "1bad72b0db980f7b283f029f7a06996ca454dadd2f7dd033bfbf3c0c004da162",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfe0ac",
        "00bfe16b"
      ]
    ],
    "bytes_sha256": "fa9960f9b9fc9544e3bf3aae383b189a13ce2ce605d626e5f529b9b5465df46c",
    "instruction_count": 48,
    "instruction_bytes": 192,
    "body_bytes": 192,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bfe0a4](../00bfe/00bfe0a4.md)

## 呼び出し先

- [00c59310](../00c59/00c59310.md)
- [00c59320](../00c59/00c59320.md)
- [00c59330](../00c59/00c59330.md)
- [00c59340](../00c59/00c59340.md)
- [00c5ae70](../00c5a/00c5ae70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1002 bytes

~~~c

long * FUN_00bfe0ac(long *param_1,undefined8 param_2)

{
  long lVar1;
  long *plVar2;
  undefined1 auStack_30 [8];
  char local_28 [4];
  uint local_24;
  
  local_24 = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_28,param_1,0);
  if (local_28[0] != '\0') {
    _ZNKSt6__ndk18ios_base6getlocEv(auStack_30,(long)param_1 + *(long *)(*param_1 + -0x18));
    plVar2 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                               (auStack_30,
                                PTR__ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9cbb0
                               );
    lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
    (**(code **)(*plVar2 + 0x48))(plVar2,*(undefined8 *)(lVar1 + 0x28),0,lVar1,&local_24,param_2);
    _ZNSt6__ndk16localeD1Ev(auStack_30);
    lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
    _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | local_24);
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfe0ac"></a> `00bfe0ac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfe0b0"></a> `00bfe0b0` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfe0b4"></a> `00bfe0b4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfe0b8"></a> `00bfe0b8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfe0bc"></a> `00bfe0bc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfe0c0"></a> `00bfe0c0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfe0c4"></a> `00bfe0c4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfe0c8"></a> `00bfe0c8` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfe0cc"></a> `00bfe0cc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfe0d0"></a> `00bfe0d0` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bfe0d4"></a> `00bfe0d4` | `bf c3 1f b8` | stur wzr,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfe0d8"></a> `00bfe0d8` | `66 73 01 94` | bl 0x00c5ae70 | `UNCONDITIONAL_CALL`
<a id="insn-00bfe0dc"></a> `00bfe0dc` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bfe0e0"></a> `00bfe0e0` | `a8 03 00 34` | cbz w8,0x00bfe154 | `CONDITIONAL_JUMP`
<a id="insn-00bfe0e4"></a> `00bfe0e4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfe0e8"></a> `00bfe0e8` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfe0ec"></a> `00bfe0ec` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bfe0f0"></a> `00bfe0f0` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfe0f4"></a> `00bfe0f4` | `87 6c 01 94` | bl 0x00c59310 | `UNCONDITIONAL_CALL`
<a id="insn-00bfe0f8"></a> `00bfe0f8` | `e1 04 00 d0` | adrp x1,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bfe0fc"></a> `00bfe0fc` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bfe100"></a> `00bfe100` | `21 d8 45 f9` | ldr x1,[x1, #0xbb0] | `FALL_THROUGH`
<a id="insn-00bfe104"></a> `00bfe104` | `87 6c 01 94` | bl 0x00c59320 | `UNCONDITIONAL_CALL`
<a id="insn-00bfe108"></a> `00bfe108` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfe10c"></a> `00bfe10c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00bfe110"></a> `00bfe110` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfe114"></a> `00bfe114` | `63 02 08 8b` | add x3,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfe118"></a> `00bfe118` | `28 25 40 f9` | ldr x8,[x9, #0x48] | `FALL_THROUGH`
<a id="insn-00bfe11c"></a> `00bfe11c` | `61 14 40 f9` | ldr x1,[x3, #0x28] | `FALL_THROUGH`
<a id="insn-00bfe120"></a> `00bfe120` | `a4 13 00 d1` | sub x4,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bfe124"></a> `00bfe124` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bfe128"></a> `00bfe128` | `e5 03 14 aa` | mov x5,x20 | `FALL_THROUGH`
<a id="insn-00bfe12c"></a> `00bfe12c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfe130"></a> `00bfe130` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bfe134"></a> `00bfe134` | `7f 6c 01 94` | bl 0x00c59330 | `UNCONDITIONAL_CALL`
<a id="insn-00bfe138"></a> `00bfe138` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfe13c"></a> `00bfe13c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfe140"></a> `00bfe140` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfe144"></a> `00bfe144` | `a8 c3 5f b8` | ldur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfe148"></a> `00bfe148` | `09 20 40 b9` | ldr w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfe14c"></a> `00bfe14c` | `21 01 08 2a` | orr w1,w9,w8 | `FALL_THROUGH`
<a id="insn-00bfe150"></a> `00bfe150` | `7c 6c 01 94` | bl 0x00c59340 | `UNCONDITIONAL_CALL`
<a id="insn-00bfe154"></a> `00bfe154` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfe158"></a> `00bfe158` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfe15c"></a> `00bfe15c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfe160"></a> `00bfe160` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfe164"></a> `00bfe164` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfe168"></a> `00bfe168` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfe0ac`](#insn-00bfe0ac) 範囲 `[['00bfe0ac', '00bfe0e3']]`
  - `CONDITIONAL_JUMP` [`00bfe0e0`](#insn-00bfe0e0) → [`00bfe154`](#insn-00bfe154)
  - `FALL_THROUGH` [`00bfe0e0`](#insn-00bfe0e0) → [`00bfe0e4`](#insn-00bfe0e4)
- ブロック [`00bfe0e4`](#insn-00bfe0e4) 範囲 `[['00bfe0e4', '00bfe153']]`
  - `FALL_THROUGH` [`00bfe150`](#insn-00bfe150) → [`00bfe154`](#insn-00bfe154)
- ブロック [`00bfe154`](#insn-00bfe154) 範囲 `[['00bfe154', '00bfe16b']]`

## 命令位置別の参照

- [`00bfe0b4`](#insn-00bfe0b4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe0b8`](#insn-00bfe0b8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe0d4`](#insn-00bfe0d4) → `Stack[-0x24]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe0d8`](#insn-00bfe0d8) → [`00c5ae70`](../00c5a/00c5ae70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae70` · 推定シンボル `None` · 推定型 `None`
- [`00bfe0dc`](#insn-00bfe0dc) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe0e0`](#insn-00bfe0e0) → [`00bfe154`](#insn-00bfe154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe0f4`](#insn-00bfe0f4) → [`00c59310`](../00c59/00c59310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59310` · 推定シンボル `None` · 推定型 `None`
- [`00bfe100`](#insn-00bfe100) → `00c9cbb0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfe100`](#insn-00bfe100) → `01128c38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bfe104`](#insn-00bfe104) → [`00c59320`](../00c59/00c59320.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59320` · 推定シンボル `None` · 推定型 `None`
- [`00bfe134`](#insn-00bfe134) → [`00c59330`](../00c59/00c59330.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59330` · 推定シンボル `None` · 推定型 `None`
- [`00bfe144`](#insn-00bfe144) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe150`](#insn-00bfe150) → [`00c59340`](../00c59/00c59340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59340` · 推定シンボル `None` · 推定型 `None`
- [`00bfe158`](#insn-00bfe158) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe15c`](#insn-00bfe15c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfe0b4`](#insn-00bfe0b4)

~~~json
{
  "source": "00bfe0b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe0b8`](#insn-00bfe0b8)

~~~json
{
  "source": "00bfe0b8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe0d4`](#insn-00bfe0d4)

~~~json
{
  "source": "00bfe0d4",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe0d8`](#insn-00bfe0d8)

~~~json
{
  "source": "00bfe0d8",
  "target": "00c5ae70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfe0dc`](#insn-00bfe0dc)

~~~json
{
  "source": "00bfe0dc",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe0e0`](#insn-00bfe0e0)

~~~json
{
  "source": "00bfe0e0",
  "target": "00bfe154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe0f4`](#insn-00bfe0f4)

~~~json
{
  "source": "00bfe0f4",
  "target": "00c59310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfe100`](#insn-00bfe100)

~~~json
{
  "source": "00bfe100",
  "target": "00c9cbb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9cbb0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfe100`](#insn-00bfe100)

~~~json
{
  "source": "00bfe100",
  "target": "01128c38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128c38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfe104`](#insn-00bfe104)

~~~json
{
  "source": "00bfe104",
  "target": "00c59320",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfe134`](#insn-00bfe134)

~~~json
{
  "source": "00bfe134",
  "target": "00c59330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfe144`](#insn-00bfe144)

~~~json
{
  "source": "00bfe144",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe150`](#insn-00bfe150)

~~~json
{
  "source": "00bfe150",
  "target": "00c59340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfe158`](#insn-00bfe158)

~~~json
{
  "source": "00bfe158",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe15c`](#insn-00bfe15c)

~~~json
{
  "source": "00bfe15c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
