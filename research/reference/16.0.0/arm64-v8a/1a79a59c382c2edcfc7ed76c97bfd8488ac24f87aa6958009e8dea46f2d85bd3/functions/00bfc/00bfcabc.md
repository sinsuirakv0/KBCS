# 00bfcabc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b80074`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80074.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-618007e3da366b96730e7152a8c468de)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfcee4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcee4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-2bb5d03f04fce242fc269063ba306a67)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfcabc",
  "name": "FUN_00bfcabc",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3f6fbd7878918f55ea8a29ea90e6cff11e99ef1b3a5f6a7118d96057aaec3b07",
  "source_text_sha256": "3f6fbd7878918f55ea8a29ea90e6cff11e99ef1b3a5f6a7118d96057aaec3b07",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfcabc",
        "00bfcb7b"
      ]
    ],
    "bytes_sha256": "a232431d87d007102de60541370cf2023bc5a7233749e916f62b838ffa035c89",
    "instruction_count": 48,
    "instruction_bytes": 192,
    "body_bytes": 192,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bfcab4](../00bfc/00bfcab4.md)

## 呼び出し先

- [00c57e70](../00c57/00c57e70.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ea0](../00c57/00c57ea0.md)
- [00c599d0](../00c59/00c599d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1002 bytes

~~~c

long * FUN_00bfcabc(long *param_1,undefined8 param_2)

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
                                PTR__ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9b710
                               );
    lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
    (**(code **)(*plVar2 + 0x28))(plVar2,*(undefined8 *)(lVar1 + 0x28),0,lVar1,&local_24,param_2);
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
<a id="insn-00bfcabc"></a> `00bfcabc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfcac0"></a> `00bfcac0` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfcac4"></a> `00bfcac4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcac8"></a> `00bfcac8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcacc"></a> `00bfcacc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfcad0"></a> `00bfcad0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfcad4"></a> `00bfcad4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfcad8"></a> `00bfcad8` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfcadc"></a> `00bfcadc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfcae0"></a> `00bfcae0` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bfcae4"></a> `00bfcae4` | `bf c3 1f b8` | stur wzr,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfcae8"></a> `00bfcae8` | `ba 73 01 94` | bl 0x00c599d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcaec"></a> `00bfcaec` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bfcaf0"></a> `00bfcaf0` | `a8 03 00 34` | cbz w8,0x00bfcb64 | `CONDITIONAL_JUMP`
<a id="insn-00bfcaf4"></a> `00bfcaf4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfcaf8"></a> `00bfcaf8` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfcafc"></a> `00bfcafc` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bfcb00"></a> `00bfcb00` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfcb04"></a> `00bfcb04` | `db 6c 01 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcb08"></a> `00bfcb08` | `e1 04 00 f0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfcb0c"></a> `00bfcb0c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bfcb10"></a> `00bfcb10` | `21 88 43 f9` | ldr x1,[x1, #0x710] | `FALL_THROUGH`
<a id="insn-00bfcb14"></a> `00bfcb14` | `db 6c 01 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcb18"></a> `00bfcb18` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfcb1c"></a> `00bfcb1c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00bfcb20"></a> `00bfcb20` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfcb24"></a> `00bfcb24` | `63 02 08 8b` | add x3,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfcb28"></a> `00bfcb28` | `28 15 40 f9` | ldr x8,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00bfcb2c"></a> `00bfcb2c` | `61 14 40 f9` | ldr x1,[x3, #0x28] | `FALL_THROUGH`
<a id="insn-00bfcb30"></a> `00bfcb30` | `a4 13 00 d1` | sub x4,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bfcb34"></a> `00bfcb34` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bfcb38"></a> `00bfcb38` | `e5 03 14 aa` | mov x5,x20 | `FALL_THROUGH`
<a id="insn-00bfcb3c"></a> `00bfcb3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfcb40"></a> `00bfcb40` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bfcb44"></a> `00bfcb44` | `d3 6c 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcb48"></a> `00bfcb48` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfcb4c"></a> `00bfcb4c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfcb50"></a> `00bfcb50` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfcb54"></a> `00bfcb54` | `a8 c3 5f b8` | ldur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfcb58"></a> `00bfcb58` | `09 20 40 b9` | ldr w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcb5c"></a> `00bfcb5c` | `21 01 08 2a` | orr w1,w9,w8 | `FALL_THROUGH`
<a id="insn-00bfcb60"></a> `00bfcb60` | `d0 6c 01 94` | bl 0x00c57ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcb64"></a> `00bfcb64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfcb68"></a> `00bfcb68` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcb6c"></a> `00bfcb6c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcb70"></a> `00bfcb70` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfcb74"></a> `00bfcb74` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfcb78"></a> `00bfcb78` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfcabc`](#insn-00bfcabc) 範囲 `[['00bfcabc', '00bfcaf3']]`
  - `CONDITIONAL_JUMP` [`00bfcaf0`](#insn-00bfcaf0) → [`00bfcb64`](#insn-00bfcb64)
  - `FALL_THROUGH` [`00bfcaf0`](#insn-00bfcaf0) → [`00bfcaf4`](#insn-00bfcaf4)
- ブロック [`00bfcaf4`](#insn-00bfcaf4) 範囲 `[['00bfcaf4', '00bfcb63']]`
  - `FALL_THROUGH` [`00bfcb60`](#insn-00bfcb60) → [`00bfcb64`](#insn-00bfcb64)
- ブロック [`00bfcb64`](#insn-00bfcb64) 範囲 `[['00bfcb64', '00bfcb7b']]`

## 命令位置別の参照

- [`00bfcac4`](#insn-00bfcac4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcac8`](#insn-00bfcac8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcae4`](#insn-00bfcae4) → `Stack[-0x24]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcae8`](#insn-00bfcae8) → [`00c599d0`](../00c59/00c599d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c599d0` · 推定シンボル `None` · 推定型 `None`
- [`00bfcaec`](#insn-00bfcaec) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcaf0`](#insn-00bfcaf0) → [`00bfcb64`](#insn-00bfcb64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcb04`](#insn-00bfcb04) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00bfcb10`](#insn-00bfcb10) → `00c9b710`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfcb10`](#insn-00bfcb10) → `01127778`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bfcb14`](#insn-00bfcb14) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00bfcb44`](#insn-00bfcb44) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bfcb54`](#insn-00bfcb54) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcb60`](#insn-00bfcb60) → [`00c57ea0`](../00c57/00c57ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bfcb68`](#insn-00bfcb68) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcb6c`](#insn-00bfcb6c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfcac4`](#insn-00bfcac4)

~~~json
{
  "source": "00bfcac4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcac8`](#insn-00bfcac8)

~~~json
{
  "source": "00bfcac8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcae4`](#insn-00bfcae4)

~~~json
{
  "source": "00bfcae4",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcae8`](#insn-00bfcae8)

~~~json
{
  "source": "00bfcae8",
  "target": "00c599d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcaec`](#insn-00bfcaec)

~~~json
{
  "source": "00bfcaec",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcaf0`](#insn-00bfcaf0)

~~~json
{
  "source": "00bfcaf0",
  "target": "00bfcb64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcb04`](#insn-00bfcb04)

~~~json
{
  "source": "00bfcb04",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcb10`](#insn-00bfcb10)

~~~json
{
  "source": "00bfcb10",
  "target": "00c9b710",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b710",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfcb10`](#insn-00bfcb10)

~~~json
{
  "source": "00bfcb10",
  "target": "01127778",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127778",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfcb14`](#insn-00bfcb14)

~~~json
{
  "source": "00bfcb14",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcb44`](#insn-00bfcb44)

~~~json
{
  "source": "00bfcb44",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcb54`](#insn-00bfcb54)

~~~json
{
  "source": "00bfcb54",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcb60`](#insn-00bfcb60)

~~~json
{
  "source": "00bfcb60",
  "target": "00c57ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcb68`](#insn-00bfcb68)

~~~json
{
  "source": "00bfcb68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcb6c`](#insn-00bfcb6c)

~~~json
{
  "source": "00bfcb6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
