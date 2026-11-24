# 00b6eebc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0173.md#review-6eebf48898122cba0f346283e35a3714)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b6f2e4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f2e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0038.md#compare-f2daca719a5c2fff3f0a4889fde6a234)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6eebc",
  "name": "_ZNK11flatbuffers6Parser15GetPooledStringERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "60055d8fc72005b7b2657688e98233b50b2a5e5637cc50e5c543fd220e0b8e14",
  "source_text_sha256": "60055d8fc72005b7b2657688e98233b50b2a5e5637cc50e5c543fd220e0b8e14",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6eebc",
        "00b6ef8f"
      ]
    ],
    "bytes_sha256": "95e99af2a3b902e95341fbb8297519b84ade354ca277e7b111ee2e3b3aff33c4",
    "instruction_count": 53,
    "instruction_bytes": 212,
    "body_bytes": 212,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0054a5d4](../0054a/0054a5d4.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5b1b0](../00c5b/00c5b1b0.md)
- [00c5b1e0](../00c5b/00c5b1e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1268 bytes

~~~c

undefined8 *
_ZNK11flatbuffers6Parser15GetPooledStringERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
          (long param_1,undefined8 param_2)

{
  long *plVar1;
  long lVar2;
  undefined8 *puVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  undefined8 local_50;
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  plVar1 = (long *)(param_1 + 0x5c8);
  puVar3 = (undefined8 *)FUN_0054a5d4(plVar1,&local_50,param_2);
  puVar5 = (undefined8 *)*puVar3;
  if (puVar5 == (undefined8 *)0x0) {
    puVar5 = (undefined8 *)_Znwm(0x38);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_(puVar5 + 4,param_2);
    *puVar5 = 0;
    puVar5[1] = 0;
    puVar5[2] = local_50;
    *puVar3 = puVar5;
    puVar4 = puVar5;
    if (*(long *)*plVar1 != 0) {
      *plVar1 = *(long *)*plVar1;
      puVar4 = (undefined8 *)*puVar3;
    }
    _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_
              (*(undefined8 *)(param_1 + 0x5d0),puVar4);
    *(long *)(param_1 + 0x5d8) = *(long *)(param_1 + 0x5d8) + 1;
  }
  if (*(long *)(lVar2 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return puVar5 + 4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6eebc"></a> `00b6eebc` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b6eec0"></a> `00b6eec0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6eec4"></a> `00b6eec4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6eec8"></a> `00b6eec8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b6eecc"></a> `00b6eecc` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b6eed0"></a> `00b6eed0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b6eed4"></a> `00b6eed4` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b6eed8"></a> `00b6eed8` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00b6eedc"></a> `00b6eedc` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00b6eee0"></a> `00b6eee0` | `15 20 17 91` | add x21,x0,#0x5c8 | `FALL_THROUGH`
<a id="insn-00b6eee4"></a> `00b6eee4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b6eee8"></a> `00b6eee8` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00b6eeec"></a> `00b6eeec` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b6eef0"></a> `00b6eef0` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00b6eef4"></a> `00b6eef4` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b6eef8"></a> `00b6eef8` | `b7 6d e7 97` | bl 0x0054a5d4 | `UNCONDITIONAL_CALL`
<a id="insn-00b6eefc"></a> `00b6eefc` | `14 00 40 f9` | ldr x20,[x0] | `FALL_THROUGH`
<a id="insn-00b6ef00"></a> `00b6ef00` | `14 03 00 b5` | cbnz x20,0x00b6ef60 | `CONDITIONAL_JUMP`
<a id="insn-00b6ef04"></a> `00b6ef04` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00b6ef08"></a> `00b6ef08` | `00 07 80 52` | mov w0,#0x38 | `FALL_THROUGH`
<a id="insn-00b6ef0c"></a> `00b6ef0c` | `e1 a2 03 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ef10"></a> `00b6ef10` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b6ef14"></a> `00b6ef14` | `00 80 00 91` | add x0,x0,#0x20 | `FALL_THROUGH`
<a id="insn-00b6ef18"></a> `00b6ef18` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00b6ef1c"></a> `00b6ef1c` | `a5 b0 03 94` | bl 0x00c5b1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ef20"></a> `00b6ef20` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00b6ef24"></a> `00b6ef24` | `9f 7e 00 a9` | stp xzr,xzr,[x20] | `FALL_THROUGH`
<a id="insn-00b6ef28"></a> `00b6ef28` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b6ef2c"></a> `00b6ef2c` | `d4 02 00 f9` | str x20,[x22] | `FALL_THROUGH`
<a id="insn-00b6ef30"></a> `00b6ef30` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00b6ef34"></a> `00b6ef34` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00b6ef38"></a> `00b6ef38` | `88 00 00 b4` | cbz x8,0x00b6ef48 | `CONDITIONAL_JUMP`
<a id="insn-00b6ef3c"></a> `00b6ef3c` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00b6ef40"></a> `00b6ef40` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00b6ef44"></a> `00b6ef44` | `02 00 00 14` | b 0x00b6ef4c | `UNCONDITIONAL_JUMP`
<a id="insn-00b6ef48"></a> `00b6ef48` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b6ef4c"></a> `00b6ef4c` | `60 ea 42 f9` | ldr x0,[x19, #0x5d0] | `FALL_THROUGH`
<a id="insn-00b6ef50"></a> `00b6ef50` | `a4 b0 03 94` | bl 0x00c5b1e0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ef54"></a> `00b6ef54` | `68 ee 42 f9` | ldr x8,[x19, #0x5d8] | `FALL_THROUGH`
<a id="insn-00b6ef58"></a> `00b6ef58` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6ef5c"></a> `00b6ef5c` | `68 ee 02 f9` | str x8,[x19, #0x5d8] | `FALL_THROUGH`
<a id="insn-00b6ef60"></a> `00b6ef60` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00b6ef64"></a> `00b6ef64` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b6ef68"></a> `00b6ef68` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b6ef6c"></a> `00b6ef6c` | `01 01 00 54` | b.ne 0x00b6ef8c | `CONDITIONAL_JUMP`
<a id="insn-00b6ef70"></a> `00b6ef70` | `80 82 00 91` | add x0,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00b6ef74"></a> `00b6ef74` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b6ef78"></a> `00b6ef78` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b6ef7c"></a> `00b6ef7c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6ef80"></a> `00b6ef80` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6ef84"></a> `00b6ef84` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b6ef88"></a> `00b6ef88` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b6ef8c"></a> `00b6ef8c` | `d5 a2 03 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6eebc`](#insn-00b6eebc) 範囲 `[['00b6eebc', '00b6ef03']]`
  - `CONDITIONAL_JUMP` [`00b6ef00`](#insn-00b6ef00) → [`00b6ef60`](#insn-00b6ef60)
  - `FALL_THROUGH` [`00b6ef00`](#insn-00b6ef00) → [`00b6ef04`](#insn-00b6ef04)
- ブロック [`00b6ef04`](#insn-00b6ef04) 範囲 `[['00b6ef04', '00b6ef3b']]`
  - `CONDITIONAL_JUMP` [`00b6ef38`](#insn-00b6ef38) → [`00b6ef48`](#insn-00b6ef48)
  - `FALL_THROUGH` [`00b6ef38`](#insn-00b6ef38) → [`00b6ef3c`](#insn-00b6ef3c)
- ブロック [`00b6ef3c`](#insn-00b6ef3c) 範囲 `[['00b6ef3c', '00b6ef47']]`
  - `UNCONDITIONAL_JUMP` [`00b6ef44`](#insn-00b6ef44) → [`00b6ef4c`](#insn-00b6ef4c)
- ブロック [`00b6ef48`](#insn-00b6ef48) 範囲 `[['00b6ef48', '00b6ef4b']]`
  - `FALL_THROUGH` [`00b6ef48`](#insn-00b6ef48) → [`00b6ef4c`](#insn-00b6ef4c)
- ブロック [`00b6ef4c`](#insn-00b6ef4c) 範囲 `[['00b6ef4c', '00b6ef5f']]`
  - `FALL_THROUGH` [`00b6ef5c`](#insn-00b6ef5c) → [`00b6ef60`](#insn-00b6ef60)
- ブロック [`00b6ef60`](#insn-00b6ef60) 範囲 `[['00b6ef60', '00b6ef6f']]`
  - `CONDITIONAL_JUMP` [`00b6ef6c`](#insn-00b6ef6c) → [`00b6ef8c`](#insn-00b6ef8c)
  - `FALL_THROUGH` [`00b6ef6c`](#insn-00b6ef6c) → [`00b6ef70`](#insn-00b6ef70)
- ブロック [`00b6ef70`](#insn-00b6ef70) 範囲 `[['00b6ef70', '00b6ef8b']]`
- ブロック [`00b6ef8c`](#insn-00b6ef8c) 範囲 `[['00b6ef8c', '00b6ef8f']]`

## 命令位置別の参照

- [`00b6eec0`](#insn-00b6eec0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eec4`](#insn-00b6eec4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eec8`](#insn-00b6eec8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eecc`](#insn-00b6eecc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eef4`](#insn-00b6eef4) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eef8`](#insn-00b6eef8) → [`0054a5d4`](../0054a/0054a5d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0054a5d4` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef00`](#insn-00b6ef00) → [`00b6ef60`](#insn-00b6ef60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef0c`](#insn-00b6ef0c) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef1c`](#insn-00b6ef1c) → [`00c5b1b0`](../00c5b/00c5b1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef20`](#insn-00b6ef20) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef38`](#insn-00b6ef38) → [`00b6ef48`](#insn-00b6ef48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef44`](#insn-00b6ef44) → [`00b6ef4c`](#insn-00b6ef4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef50`](#insn-00b6ef50) → [`00c5b1e0`](../00c5b/00c5b1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b1e0` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef64`](#insn-00b6ef64) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef6c`](#insn-00b6ef6c) → [`00b6ef8c`](#insn-00b6ef8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef74`](#insn-00b6ef74) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef78`](#insn-00b6ef78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef7c`](#insn-00b6ef7c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef80`](#insn-00b6ef80) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef8c`](#insn-00b6ef8c) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6eec0`](#insn-00b6eec0)

~~~json
{
  "source": "00b6eec0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eec4`](#insn-00b6eec4)

~~~json
{
  "source": "00b6eec4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eec8`](#insn-00b6eec8)

~~~json
{
  "source": "00b6eec8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eecc`](#insn-00b6eecc)

~~~json
{
  "source": "00b6eecc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eef4`](#insn-00b6eef4)

~~~json
{
  "source": "00b6eef4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eef8`](#insn-00b6eef8)

~~~json
{
  "source": "00b6eef8",
  "target": "0054a5d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ef00`](#insn-00b6ef00)

~~~json
{
  "source": "00b6ef00",
  "target": "00b6ef60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ef0c`](#insn-00b6ef0c)

~~~json
{
  "source": "00b6ef0c",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ef1c`](#insn-00b6ef1c)

~~~json
{
  "source": "00b6ef1c",
  "target": "00c5b1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ef20`](#insn-00b6ef20)

~~~json
{
  "source": "00b6ef20",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ef38`](#insn-00b6ef38)

~~~json
{
  "source": "00b6ef38",
  "target": "00b6ef48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ef44`](#insn-00b6ef44)

~~~json
{
  "source": "00b6ef44",
  "target": "00b6ef4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ef50`](#insn-00b6ef50)

~~~json
{
  "source": "00b6ef50",
  "target": "00c5b1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ef64`](#insn-00b6ef64)

~~~json
{
  "source": "00b6ef64",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ef6c`](#insn-00b6ef6c)

~~~json
{
  "source": "00b6ef6c",
  "target": "00b6ef8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ef74`](#insn-00b6ef74)

~~~json
{
  "source": "00b6ef74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ef78`](#insn-00b6ef78)

~~~json
{
  "source": "00b6ef78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ef7c`](#insn-00b6ef7c)

~~~json
{
  "source": "00b6ef7c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ef80`](#insn-00b6ef80)

~~~json
{
  "source": "00b6ef80",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ef8c`](#insn-00b6ef8c)

~~~json
{
  "source": "00b6ef8c",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
