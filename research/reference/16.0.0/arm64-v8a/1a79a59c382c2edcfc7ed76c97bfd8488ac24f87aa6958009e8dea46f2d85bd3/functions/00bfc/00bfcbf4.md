# 00bfcbf4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b801ac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b801ac.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-d7a26254b2f953402823e71c3b8dde68)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfd01c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd01c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-20a6661b477b572dc9e1bd197e45847e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfcbf4",
  "name": "FUN_00bfcbf4",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f45776185b7886b7c694171fb153cdbe87fb2abf62e0322f9290c4d8c02ed64f",
  "source_text_sha256": "f45776185b7886b7c694171fb153cdbe87fb2abf62e0322f9290c4d8c02ed64f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfcbf4",
        "00bfccb3"
      ]
    ],
    "bytes_sha256": "d2fc44aff55fe31dbf0de731f87b601b9049cd3f37959599e8bc01b7eb016434",
    "instruction_count": 48,
    "instruction_bytes": 192,
    "body_bytes": 192,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bfcbec](../00bfc/00bfcbec.md)

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

long * FUN_00bfcbf4(long *param_1,undefined8 param_2)

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
<a id="insn-00bfcbf4"></a> `00bfcbf4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfcbf8"></a> `00bfcbf8` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfcbfc"></a> `00bfcbfc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcc00"></a> `00bfcc00` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcc04"></a> `00bfcc04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfcc08"></a> `00bfcc08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfcc0c"></a> `00bfcc0c` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfcc10"></a> `00bfcc10` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfcc14"></a> `00bfcc14` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfcc18"></a> `00bfcc18` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bfcc1c"></a> `00bfcc1c` | `bf c3 1f b8` | stur wzr,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfcc20"></a> `00bfcc20` | `6c 73 01 94` | bl 0x00c599d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcc24"></a> `00bfcc24` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bfcc28"></a> `00bfcc28` | `a8 03 00 34` | cbz w8,0x00bfcc9c | `CONDITIONAL_JUMP`
<a id="insn-00bfcc2c"></a> `00bfcc2c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfcc30"></a> `00bfcc30` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfcc34"></a> `00bfcc34` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bfcc38"></a> `00bfcc38` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfcc3c"></a> `00bfcc3c` | `8d 6c 01 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcc40"></a> `00bfcc40` | `e1 04 00 f0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfcc44"></a> `00bfcc44` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bfcc48"></a> `00bfcc48` | `21 88 43 f9` | ldr x1,[x1, #0x710] | `FALL_THROUGH`
<a id="insn-00bfcc4c"></a> `00bfcc4c` | `8d 6c 01 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcc50"></a> `00bfcc50` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfcc54"></a> `00bfcc54` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00bfcc58"></a> `00bfcc58` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfcc5c"></a> `00bfcc5c` | `63 02 08 8b` | add x3,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfcc60"></a> `00bfcc60` | `28 25 40 f9` | ldr x8,[x9, #0x48] | `FALL_THROUGH`
<a id="insn-00bfcc64"></a> `00bfcc64` | `61 14 40 f9` | ldr x1,[x3, #0x28] | `FALL_THROUGH`
<a id="insn-00bfcc68"></a> `00bfcc68` | `a4 13 00 d1` | sub x4,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bfcc6c"></a> `00bfcc6c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bfcc70"></a> `00bfcc70` | `e5 03 14 aa` | mov x5,x20 | `FALL_THROUGH`
<a id="insn-00bfcc74"></a> `00bfcc74` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfcc78"></a> `00bfcc78` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bfcc7c"></a> `00bfcc7c` | `85 6c 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcc80"></a> `00bfcc80` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfcc84"></a> `00bfcc84` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfcc88"></a> `00bfcc88` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfcc8c"></a> `00bfcc8c` | `a8 c3 5f b8` | ldur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfcc90"></a> `00bfcc90` | `09 20 40 b9` | ldr w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcc94"></a> `00bfcc94` | `21 01 08 2a` | orr w1,w9,w8 | `FALL_THROUGH`
<a id="insn-00bfcc98"></a> `00bfcc98` | `82 6c 01 94` | bl 0x00c57ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcc9c"></a> `00bfcc9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfcca0"></a> `00bfcca0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcca4"></a> `00bfcca4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcca8"></a> `00bfcca8` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfccac"></a> `00bfccac` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfccb0"></a> `00bfccb0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfcbf4`](#insn-00bfcbf4) 範囲 `[['00bfcbf4', '00bfcc2b']]`
  - `CONDITIONAL_JUMP` [`00bfcc28`](#insn-00bfcc28) → [`00bfcc9c`](#insn-00bfcc9c)
  - `FALL_THROUGH` [`00bfcc28`](#insn-00bfcc28) → [`00bfcc2c`](#insn-00bfcc2c)
- ブロック [`00bfcc2c`](#insn-00bfcc2c) 範囲 `[['00bfcc2c', '00bfcc9b']]`
  - `FALL_THROUGH` [`00bfcc98`](#insn-00bfcc98) → [`00bfcc9c`](#insn-00bfcc9c)
- ブロック [`00bfcc9c`](#insn-00bfcc9c) 範囲 `[['00bfcc9c', '00bfccb3']]`

## 命令位置別の参照

- [`00bfcbfc`](#insn-00bfcbfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc00`](#insn-00bfcc00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc1c`](#insn-00bfcc1c) → `Stack[-0x24]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc20`](#insn-00bfcc20) → [`00c599d0`](../00c59/00c599d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c599d0` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc24`](#insn-00bfcc24) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc28`](#insn-00bfcc28) → [`00bfcc9c`](#insn-00bfcc9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc3c`](#insn-00bfcc3c) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc48`](#insn-00bfcc48) → `00c9b710`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfcc48`](#insn-00bfcc48) → `01127778`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bfcc4c`](#insn-00bfcc4c) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc7c`](#insn-00bfcc7c) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc8c`](#insn-00bfcc8c) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc98`](#insn-00bfcc98) → [`00c57ea0`](../00c57/00c57ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bfcca0`](#insn-00bfcca0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcca4`](#insn-00bfcca4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfcbfc`](#insn-00bfcbfc)

~~~json
{
  "source": "00bfcbfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcc00`](#insn-00bfcc00)

~~~json
{
  "source": "00bfcc00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcc1c`](#insn-00bfcc1c)

~~~json
{
  "source": "00bfcc1c",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcc20`](#insn-00bfcc20)

~~~json
{
  "source": "00bfcc20",
  "target": "00c599d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcc24`](#insn-00bfcc24)

~~~json
{
  "source": "00bfcc24",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcc28`](#insn-00bfcc28)

~~~json
{
  "source": "00bfcc28",
  "target": "00bfcc9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcc3c`](#insn-00bfcc3c)

~~~json
{
  "source": "00bfcc3c",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcc48`](#insn-00bfcc48)

~~~json
{
  "source": "00bfcc48",
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
- 参照命令 [`00bfcc48`](#insn-00bfcc48)

~~~json
{
  "source": "00bfcc48",
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
- 参照命令 [`00bfcc4c`](#insn-00bfcc4c)

~~~json
{
  "source": "00bfcc4c",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcc7c`](#insn-00bfcc7c)

~~~json
{
  "source": "00bfcc7c",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcc8c`](#insn-00bfcc8c)

~~~json
{
  "source": "00bfcc8c",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcc98`](#insn-00bfcc98)

~~~json
{
  "source": "00bfcc98",
  "target": "00c57ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcca0`](#insn-00bfcca0)

~~~json
{
  "source": "00bfcca0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcca4`](#insn-00bfcca4)

~~~json
{
  "source": "00bfcca4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
