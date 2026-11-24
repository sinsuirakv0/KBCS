# 00bfcf9c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b80554`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80554.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-2d56fc8fa9579be0daccf9777ff74b9e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfd3c4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd3c4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-fe661250ec935fcbf15927b9aa25b3ae)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfcf9c",
  "name": "FUN_00bfcf9c",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3e8af12411e25ed798f7283bd3fc27abb72ea33b76e22c09f48e414333774120",
  "source_text_sha256": "3e8af12411e25ed798f7283bd3fc27abb72ea33b76e22c09f48e414333774120",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfcf9c",
        "00bfd05b"
      ]
    ],
    "bytes_sha256": "2b1e92dcf32ce6fdc76d1de4c0feccb2a5b4bf6039dd9ebc3ae23ce6938c75a7",
    "instruction_count": 48,
    "instruction_bytes": 192,
    "body_bytes": 192,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bfcf94](../00bfc/00bfcf94.md)

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

long * FUN_00bfcf9c(long *param_1,undefined8 param_2)

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
    (**(code **)(*plVar2 + 0x60))(plVar2,*(undefined8 *)(lVar1 + 0x28),0,lVar1,&local_24,param_2);
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
<a id="insn-00bfcf9c"></a> `00bfcf9c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfcfa0"></a> `00bfcfa0` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfcfa4"></a> `00bfcfa4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcfa8"></a> `00bfcfa8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcfac"></a> `00bfcfac` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfcfb0"></a> `00bfcfb0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfcfb4"></a> `00bfcfb4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfcfb8"></a> `00bfcfb8` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfcfbc"></a> `00bfcfbc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfcfc0"></a> `00bfcfc0` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bfcfc4"></a> `00bfcfc4` | `bf c3 1f b8` | stur wzr,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfcfc8"></a> `00bfcfc8` | `82 72 01 94` | bl 0x00c599d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcfcc"></a> `00bfcfcc` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bfcfd0"></a> `00bfcfd0` | `a8 03 00 34` | cbz w8,0x00bfd044 | `CONDITIONAL_JUMP`
<a id="insn-00bfcfd4"></a> `00bfcfd4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfcfd8"></a> `00bfcfd8` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfcfdc"></a> `00bfcfdc` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bfcfe0"></a> `00bfcfe0` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfcfe4"></a> `00bfcfe4` | `a3 6b 01 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcfe8"></a> `00bfcfe8` | `e1 04 00 f0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfcfec"></a> `00bfcfec` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bfcff0"></a> `00bfcff0` | `21 88 43 f9` | ldr x1,[x1, #0x710] | `FALL_THROUGH`
<a id="insn-00bfcff4"></a> `00bfcff4` | `a3 6b 01 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcff8"></a> `00bfcff8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfcffc"></a> `00bfcffc` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00bfd000"></a> `00bfd000` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfd004"></a> `00bfd004` | `63 02 08 8b` | add x3,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfd008"></a> `00bfd008` | `28 31 40 f9` | ldr x8,[x9, #0x60] | `FALL_THROUGH`
<a id="insn-00bfd00c"></a> `00bfd00c` | `61 14 40 f9` | ldr x1,[x3, #0x28] | `FALL_THROUGH`
<a id="insn-00bfd010"></a> `00bfd010` | `a4 13 00 d1` | sub x4,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bfd014"></a> `00bfd014` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bfd018"></a> `00bfd018` | `e5 03 14 aa` | mov x5,x20 | `FALL_THROUGH`
<a id="insn-00bfd01c"></a> `00bfd01c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfd020"></a> `00bfd020` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bfd024"></a> `00bfd024` | `9b 6b 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bfd028"></a> `00bfd028` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfd02c"></a> `00bfd02c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfd030"></a> `00bfd030` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfd034"></a> `00bfd034` | `a8 c3 5f b8` | ldur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfd038"></a> `00bfd038` | `09 20 40 b9` | ldr w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfd03c"></a> `00bfd03c` | `21 01 08 2a` | orr w1,w9,w8 | `FALL_THROUGH`
<a id="insn-00bfd040"></a> `00bfd040` | `98 6b 01 94` | bl 0x00c57ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfd044"></a> `00bfd044` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfd048"></a> `00bfd048` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfd04c"></a> `00bfd04c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfd050"></a> `00bfd050` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfd054"></a> `00bfd054` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfd058"></a> `00bfd058` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfcf9c`](#insn-00bfcf9c) 範囲 `[['00bfcf9c', '00bfcfd3']]`
  - `CONDITIONAL_JUMP` [`00bfcfd0`](#insn-00bfcfd0) → [`00bfd044`](#insn-00bfd044)
  - `FALL_THROUGH` [`00bfcfd0`](#insn-00bfcfd0) → [`00bfcfd4`](#insn-00bfcfd4)
- ブロック [`00bfcfd4`](#insn-00bfcfd4) 範囲 `[['00bfcfd4', '00bfd043']]`
  - `FALL_THROUGH` [`00bfd040`](#insn-00bfd040) → [`00bfd044`](#insn-00bfd044)
- ブロック [`00bfd044`](#insn-00bfd044) 範囲 `[['00bfd044', '00bfd05b']]`

## 命令位置別の参照

- [`00bfcfa4`](#insn-00bfcfa4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcfa8`](#insn-00bfcfa8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcfc4`](#insn-00bfcfc4) → `Stack[-0x24]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcfc8`](#insn-00bfcfc8) → [`00c599d0`](../00c59/00c599d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c599d0` · 推定シンボル `None` · 推定型 `None`
- [`00bfcfcc`](#insn-00bfcfcc) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcfd0`](#insn-00bfcfd0) → [`00bfd044`](#insn-00bfd044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcfe4`](#insn-00bfcfe4) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00bfcff0`](#insn-00bfcff0) → `00c9b710`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfcff0`](#insn-00bfcff0) → `01127778`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bfcff4`](#insn-00bfcff4) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00bfd024`](#insn-00bfd024) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bfd034`](#insn-00bfd034) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd040`](#insn-00bfd040) → [`00c57ea0`](../00c57/00c57ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bfd048`](#insn-00bfd048) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd04c`](#insn-00bfd04c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfcfa4`](#insn-00bfcfa4)

~~~json
{
  "source": "00bfcfa4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcfa8`](#insn-00bfcfa8)

~~~json
{
  "source": "00bfcfa8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcfc4`](#insn-00bfcfc4)

~~~json
{
  "source": "00bfcfc4",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcfc8`](#insn-00bfcfc8)

~~~json
{
  "source": "00bfcfc8",
  "target": "00c599d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcfcc`](#insn-00bfcfcc)

~~~json
{
  "source": "00bfcfcc",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcfd0`](#insn-00bfcfd0)

~~~json
{
  "source": "00bfcfd0",
  "target": "00bfd044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcfe4`](#insn-00bfcfe4)

~~~json
{
  "source": "00bfcfe4",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcff0`](#insn-00bfcff0)

~~~json
{
  "source": "00bfcff0",
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
- 参照命令 [`00bfcff0`](#insn-00bfcff0)

~~~json
{
  "source": "00bfcff0",
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
- 参照命令 [`00bfcff4`](#insn-00bfcff4)

~~~json
{
  "source": "00bfcff4",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfd024`](#insn-00bfd024)

~~~json
{
  "source": "00bfd024",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfd034`](#insn-00bfd034)

~~~json
{
  "source": "00bfd034",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd040`](#insn-00bfd040)

~~~json
{
  "source": "00bfd040",
  "target": "00c57ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfd048`](#insn-00bfd048)

~~~json
{
  "source": "00bfd048",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd04c`](#insn-00bfd04c)

~~~json
{
  "source": "00bfd04c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
