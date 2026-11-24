# 00afca1c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afc9d8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc9d8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0008.md#compare-1330c214fac95c849f80a84c85e4bd5c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5c7a0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c7a0.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0060.md#compare-1a2a69c5d0afe220445c7430272243fd)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afca1c",
  "name": "_ZN8firebase15CleanupNotifier15UnregisterOwnerEPS0_Pv",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b620b0fceecefbdced7de3aa7d59bc9c69701e1a4cf19b763a35a7108d72f10d",
  "source_text_sha256": "b620b0fceecefbdced7de3aa7d59bc9c69701e1a4cf19b763a35a7108d72f10d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afca1c",
        "00afca97"
      ]
    ],
    "bytes_sha256": "b0cbff366bd62502cd1962753a95cbe359c47a8acd624a1d6953d848b742e88d",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddc20](../00bdd/00bddc20.md)
- [00bddc30](../00bdd/00bddc30.md)
- [00bdece0](../00bde/00bdece0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1309 bytes

~~~c

void _ZN8firebase15CleanupNotifier15UnregisterOwnerEPS0_Pv(undefined8 param_1,ulong param_2)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  undefined8 uVar4;
  
  uVar4 = *(undefined8 *)
           PTR__ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E_00c1b998;
  _ZN8firebase5Mutex7AcquireEv(uVar4);
                    /* try { // try from 00afca40 to 00bfca47 has its CatchHandler @ 00aff42c */
  plVar2 = (long *)(*(long *)
                     PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c1b990 + 8);
  plVar3 = (long *)*plVar2;
  plVar1 = plVar2;
  if (plVar3 != (long *)0x0) {
    do {
      if ((ulong)plVar3[4] >= param_2) {
        plVar1 = plVar3;
      }
      plVar3 = (long *)plVar3[(ulong)plVar3[4] < param_2];
    } while (plVar3 != (long *)0x0);
                    /* try { // try from 00afca70 to 00bfca87 has its CatchHandler @ 00aff428 */
    if ((plVar1 != plVar2) && ((ulong)plVar1[4] <= param_2)) {
      _ZN8firebase15CleanupNotifier15UnregisterOwnerENSt6__ndk114__map_iteratorINS1_15__tree_iteratorINS1_12__value_typeIPvPS0_EEPNS1_11__tree_nodeIS7_S5_EElEEEE
                ();
    }
  }
                    /* try { // try from 00afca88 to 00bfcb2b has its CatchHandler @ 00af5650 */
  _ZN8firebase5Mutex7ReleaseEv(uVar4);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afca1c"></a> `00afca1c` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afca20"></a> `00afca20` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afca24"></a> `00afca24` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00afca28"></a> `00afca28` | `e8 08 00 f0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00afca2c"></a> `00afca2c` | `08 cd 44 f9` | ldr x8,[x8, #0x998] | `FALL_THROUGH`
<a id="insn-00afca30"></a> `00afca30` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00afca34"></a> `00afca34` | `13 01 40 f9` | ldr x19,[x8] | `FALL_THROUGH`
<a id="insn-00afca38"></a> `00afca38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afca3c"></a> `00afca3c` | `79 84 03 94` | bl 0x00bddc20 | `UNCONDITIONAL_CALL`
<a id="insn-00afca40"></a> `00afca40` | `e8 08 00 f0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00afca44"></a> `00afca44` | `08 c9 44 f9` | ldr x8,[x8, #0x990] | `FALL_THROUGH`
<a id="insn-00afca48"></a> `00afca48` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00afca4c"></a> `00afca4c` | `09 8d 40 f8` | ldr x9,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00afca50"></a> `00afca50` | `c9 01 00 b4` | cbz x9,0x00afca88 | `CONDITIONAL_JUMP`
<a id="insn-00afca54"></a> `00afca54` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00afca58"></a> `00afca58` | `2a 11 40 f9` | ldr x10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00afca5c"></a> `00afca5c` | `5f 01 14 eb` | cmp x10,x20 | `FALL_THROUGH`
<a id="insn-00afca60"></a> `00afca60` | `ea 27 9f 1a` | cset w10,cc | `FALL_THROUGH`
<a id="insn-00afca64"></a> `00afca64` | `00 30 89 9a` | csel x0,x0,x9,cc | `FALL_THROUGH`
<a id="insn-00afca68"></a> `00afca68` | `29 59 6a f8` | ldr x9,[x9, w10, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00afca6c"></a> `00afca6c` | `69 ff ff b5` | cbnz x9,0x00afca58 | `CONDITIONAL_JUMP`
<a id="insn-00afca70"></a> `00afca70` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00afca74"></a> `00afca74` | `a0 00 00 54` | b.eq 0x00afca88 | `CONDITIONAL_JUMP`
<a id="insn-00afca78"></a> `00afca78` | `08 10 40 f9` | ldr x8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00afca7c"></a> `00afca7c` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00afca80"></a> `00afca80` | `48 00 00 54` | b.hi 0x00afca88 | `CONDITIONAL_JUMP`
<a id="insn-00afca84"></a> `00afca84` | `97 88 03 94` | bl 0x00bdece0 | `UNCONDITIONAL_CALL`
<a id="insn-00afca88"></a> `00afca88` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afca8c"></a> `00afca8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afca90"></a> `00afca90` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afca94"></a> `00afca94` | `67 84 03 14` | b 0x00bddc30 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afca1c`](#insn-00afca1c) 範囲 `[['00afca1c', '00afca3f']]`
  - `FALL_THROUGH` [`00afca3c`](#insn-00afca3c) → [`00afca40`](#insn-00afca40)
- ブロック [`00afca40`](#insn-00afca40) 範囲 `[['00afca40', '00afca53']]`
  - `CONDITIONAL_JUMP` [`00afca50`](#insn-00afca50) → [`00afca88`](#insn-00afca88)
  - `FALL_THROUGH` [`00afca50`](#insn-00afca50) → [`00afca54`](#insn-00afca54)
- ブロック [`00afca54`](#insn-00afca54) 範囲 `[['00afca54', '00afca57']]`
  - `FALL_THROUGH` [`00afca54`](#insn-00afca54) → [`00afca58`](#insn-00afca58)
- ブロック [`00afca58`](#insn-00afca58) 範囲 `[['00afca58', '00afca6f']]`
  - `CONDITIONAL_JUMP` [`00afca6c`](#insn-00afca6c) → [`00afca58`](#insn-00afca58)
  - `FALL_THROUGH` [`00afca6c`](#insn-00afca6c) → [`00afca70`](#insn-00afca70)
- ブロック [`00afca70`](#insn-00afca70) 範囲 `[['00afca70', '00afca77']]`
  - `CONDITIONAL_JUMP` [`00afca74`](#insn-00afca74) → [`00afca88`](#insn-00afca88)
  - `FALL_THROUGH` [`00afca74`](#insn-00afca74) → [`00afca78`](#insn-00afca78)
- ブロック [`00afca78`](#insn-00afca78) 範囲 `[['00afca78', '00afca83']]`
  - `CONDITIONAL_JUMP` [`00afca80`](#insn-00afca80) → [`00afca88`](#insn-00afca88)
  - `FALL_THROUGH` [`00afca80`](#insn-00afca80) → [`00afca84`](#insn-00afca84)
- ブロック [`00afca84`](#insn-00afca84) 範囲 `[['00afca84', '00afca87']]`
  - `FALL_THROUGH` [`00afca84`](#insn-00afca84) → [`00afca88`](#insn-00afca88)
- ブロック [`00afca88`](#insn-00afca88) 範囲 `[['00afca88', '00afca97']]`

## 命令位置別の参照

- [`00afca1c`](#insn-00afca1c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afca20`](#insn-00afca20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afca2c`](#insn-00afca2c) → `00c1b998`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00afca34`](#insn-00afca34) → `010a0d48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E` · 推定型 `undefined8`
- [`00afca3c`](#insn-00afca3c) → [`00bddc20`](../00bdd/00bddc20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc20` · 推定シンボル `None` · 推定型 `None`
- [`00afca44`](#insn-00afca44) → `00c1b990`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00afca48`](#insn-00afca48) → `010a0d50`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E` · 推定型 `undefined8`
- [`00afca50`](#insn-00afca50) → [`00afca88`](#insn-00afca88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afca6c`](#insn-00afca6c) → [`00afca58`](#insn-00afca58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afca74`](#insn-00afca74) → [`00afca88`](#insn-00afca88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afca80`](#insn-00afca80) → [`00afca88`](#insn-00afca88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afca84`](#insn-00afca84) → [`00bdece0`](../00bde/00bdece0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdece0` · 推定シンボル `None` · 推定型 `None`
- [`00afca88`](#insn-00afca88) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afca94`](#insn-00afca94) → [`00bddc30`](../00bdd/00bddc30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc30` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afca1c`](#insn-00afca1c)

~~~json
{
  "source": "00afca1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afca20`](#insn-00afca20)

~~~json
{
  "source": "00afca20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afca2c`](#insn-00afca2c)

~~~json
{
  "source": "00afca2c",
  "target": "00c1b998",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b998",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afca34`](#insn-00afca34)

~~~json
{
  "source": "00afca34",
  "target": "010a0d48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afca3c`](#insn-00afca3c)

~~~json
{
  "source": "00afca3c",
  "target": "00bddc20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afca44`](#insn-00afca44)

~~~json
{
  "source": "00afca44",
  "target": "00c1b990",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b990",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afca48`](#insn-00afca48)

~~~json
{
  "source": "00afca48",
  "target": "010a0d50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afca50`](#insn-00afca50)

~~~json
{
  "source": "00afca50",
  "target": "00afca88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afca6c`](#insn-00afca6c)

~~~json
{
  "source": "00afca6c",
  "target": "00afca58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afca74`](#insn-00afca74)

~~~json
{
  "source": "00afca74",
  "target": "00afca88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afca80`](#insn-00afca80)

~~~json
{
  "source": "00afca80",
  "target": "00afca88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afca84`](#insn-00afca84)

~~~json
{
  "source": "00afca84",
  "target": "00bdece0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afca88`](#insn-00afca88)

~~~json
{
  "source": "00afca88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afca94`](#insn-00afca94)

~~~json
{
  "source": "00afca94",
  "target": "00bddc30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
