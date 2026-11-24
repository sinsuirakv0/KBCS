# 00accaec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acbaf8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbaf8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-1fe077051b4208b35b07a2a3bcb74a1d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00accaec",
  "name": "FUN_00accaec",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ca5480be226db2febdfed61ef3320dd9fc85aff8bc70144bf6964548685bdf32",
  "source_text_sha256": "ca5480be226db2febdfed61ef3320dd9fc85aff8bc70144bf6964548685bdf32",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00accaec",
        "00accbbf"
      ]
    ],
    "bytes_sha256": "977ebf7b1ec25d1630d8cd58909a964564c5e10151f54bf460adfad377faffdf",
    "instruction_count": 53,
    "instruction_bytes": 212,
    "body_bytes": 212,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00732374](../00732/00732374.md)
- [007323d0](../00732/007323d0.md)
- [00936950](../00936/00936950.md)
- [009369dc](../00936/009369dc.md)
- [00acd07c](../00acd/00acd07c.md)
- [00acd0dc](../00acd/00acd0dc.md)

## 呼び出し先

- [00c54d90](../00c54/00c54d90.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f50](../00c58/00c58f50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1049 bytes

~~~c

void FUN_00accaec(undefined8 *param_1)

{
  void *__ptr;
  long lVar1;
  long *plVar2;
  void *pvVar3;
  void *pvVar4;
  
  pvVar3 = (void *)param_1[8];
  *param_1 = &PTR_FUN_00c8e960;
  if (pvVar3 != (void *)0x0) {
    pvVar4 = (void *)param_1[9];
    __ptr = pvVar3;
    if (pvVar4 != pvVar3) {
      do {
        plVar2 = *(long **)((long)pvVar4 + -8);
        if ((plVar2 != (long *)0x0) &&
           (lVar1 = FUN_00c54d90(0xffffffffffffffff,plVar2 + 1), lVar1 == 0)) {
          (**(code **)(*plVar2 + 0x10))(plVar2);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
        }
        pvVar4 = (void *)((long)pvVar4 + -0x10);
      } while (pvVar4 != pvVar3);
      __ptr = (void *)param_1[8];
    }
    param_1[9] = pvVar3;
    _ZdlPv(__ptr);
  }
  plVar2 = (long *)param_1[7];
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c54d90(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00accaec"></a> `00accaec` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00accaf0"></a> `00accaf0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00accaf4"></a> `00accaf4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00accaf8"></a> `00accaf8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00accafc"></a> `00accafc` | `15 20 40 f9` | ldr x21,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00accb00"></a> `00accb00` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00accb04"></a> `00accb04` | `08 0e 00 d0` | adrp x8,0xc8e000 | `FALL_THROUGH`
<a id="insn-00accb08"></a> `00accb08` | `08 81 25 91` | add x8,x8,#0x960 | `FALL_THROUGH`
<a id="insn-00accb0c"></a> `00accb0c` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00accb10"></a> `00accb10` | `35 03 00 b4` | cbz x21,0x00accb74 | `CONDITIONAL_JUMP`
<a id="insn-00accb14"></a> `00accb14` | `76 26 40 f9` | ldr x22,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00accb18"></a> `00accb18` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00accb1c"></a> `00accb1c` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-00accb20"></a> `00accb20` | `a1 00 00 54` | b.ne 0x00accb34 | `CONDITIONAL_JUMP`
<a id="insn-00accb24"></a> `00accb24` | `12 00 00 14` | b 0x00accb6c | `UNCONDITIONAL_JUMP`
<a id="insn-00accb28"></a> `00accb28` | `d6 42 00 d1` | sub x22,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00accb2c"></a> `00accb2c` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-00accb30"></a> `00accb30` | `c0 01 00 54` | b.eq 0x00accb68 | `CONDITIONAL_JUMP`
<a id="insn-00accb34"></a> `00accb34` | `d4 82 5f f8` | ldur x20,[x22, #-0x8] | `FALL_THROUGH`
<a id="insn-00accb38"></a> `00accb38` | `94 ff ff b4` | cbz x20,0x00accb28 | `CONDITIONAL_JUMP`
<a id="insn-00accb3c"></a> `00accb3c` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00accb40"></a> `00accb40` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00accb44"></a> `00accb44` | `93 20 06 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-00accb48"></a> `00accb48` | `00 ff ff b5` | cbnz x0,0x00accb28 | `CONDITIONAL_JUMP`
<a id="insn-00accb4c"></a> `00accb4c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00accb50"></a> `00accb50` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00accb54"></a> `00accb54` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00accb58"></a> `00accb58` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00accb5c"></a> `00accb5c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00accb60"></a> `00accb60` | `f0 30 06 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-00accb64"></a> `00accb64` | `f1 ff ff 17` | b 0x00accb28 | `UNCONDITIONAL_JUMP`
<a id="insn-00accb68"></a> `00accb68` | `60 22 40 f9` | ldr x0,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00accb6c"></a> `00accb6c` | `75 26 00 f9` | str x21,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00accb70"></a> `00accb70` | `f8 30 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00accb74"></a> `00accb74` | `73 1e 40 f9` | ldr x19,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00accb78"></a> `00accb78` | `b3 00 00 b4` | cbz x19,0x00accb8c | `CONDITIONAL_JUMP`
<a id="insn-00accb7c"></a> `00accb7c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00accb80"></a> `00accb80` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00accb84"></a> `00accb84` | `83 20 06 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-00accb88"></a> `00accb88` | `a0 00 00 b4` | cbz x0,0x00accb9c | `CONDITIONAL_JUMP`
<a id="insn-00accb8c"></a> `00accb8c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00accb90"></a> `00accb90` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00accb94"></a> `00accb94` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00accb98"></a> `00accb98` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00accb9c"></a> `00accb9c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00accba0"></a> `00accba0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00accba4"></a> `00accba4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00accba8"></a> `00accba8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00accbac"></a> `00accbac` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00accbb0"></a> `00accbb0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00accbb4"></a> `00accbb4` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00accbb8"></a> `00accbb8` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00accbbc"></a> `00accbbc` | `d9 30 06 14` | b 0x00c58f20 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00accaec`](#insn-00accaec) 範囲 `[['00accaec', '00accb13']]`
  - `CONDITIONAL_JUMP` [`00accb10`](#insn-00accb10) → [`00accb74`](#insn-00accb74)
  - `FALL_THROUGH` [`00accb10`](#insn-00accb10) → [`00accb14`](#insn-00accb14)
- ブロック [`00accb14`](#insn-00accb14) 範囲 `[['00accb14', '00accb23']]`
  - `CONDITIONAL_JUMP` [`00accb20`](#insn-00accb20) → [`00accb34`](#insn-00accb34)
  - `FALL_THROUGH` [`00accb20`](#insn-00accb20) → [`00accb24`](#insn-00accb24)
- ブロック [`00accb24`](#insn-00accb24) 範囲 `[['00accb24', '00accb27']]`
  - `UNCONDITIONAL_JUMP` [`00accb24`](#insn-00accb24) → [`00accb6c`](#insn-00accb6c)
- ブロック [`00accb28`](#insn-00accb28) 範囲 `[['00accb28', '00accb33']]`
  - `CONDITIONAL_JUMP` [`00accb30`](#insn-00accb30) → [`00accb68`](#insn-00accb68)
  - `FALL_THROUGH` [`00accb30`](#insn-00accb30) → [`00accb34`](#insn-00accb34)
- ブロック [`00accb34`](#insn-00accb34) 範囲 `[['00accb34', '00accb3b']]`
  - `CONDITIONAL_JUMP` [`00accb38`](#insn-00accb38) → [`00accb28`](#insn-00accb28)
  - `FALL_THROUGH` [`00accb38`](#insn-00accb38) → [`00accb3c`](#insn-00accb3c)
- ブロック [`00accb3c`](#insn-00accb3c) 範囲 `[['00accb3c', '00accb4b']]`
  - `CONDITIONAL_JUMP` [`00accb48`](#insn-00accb48) → [`00accb28`](#insn-00accb28)
  - `FALL_THROUGH` [`00accb48`](#insn-00accb48) → [`00accb4c`](#insn-00accb4c)
- ブロック [`00accb4c`](#insn-00accb4c) 範囲 `[['00accb4c', '00accb67']]`
  - `UNCONDITIONAL_JUMP` [`00accb64`](#insn-00accb64) → [`00accb28`](#insn-00accb28)
- ブロック [`00accb68`](#insn-00accb68) 範囲 `[['00accb68', '00accb6b']]`
  - `FALL_THROUGH` [`00accb68`](#insn-00accb68) → [`00accb6c`](#insn-00accb6c)
- ブロック [`00accb6c`](#insn-00accb6c) 範囲 `[['00accb6c', '00accb73']]`
  - `FALL_THROUGH` [`00accb70`](#insn-00accb70) → [`00accb74`](#insn-00accb74)
- ブロック [`00accb74`](#insn-00accb74) 範囲 `[['00accb74', '00accb7b']]`
  - `CONDITIONAL_JUMP` [`00accb78`](#insn-00accb78) → [`00accb8c`](#insn-00accb8c)
  - `FALL_THROUGH` [`00accb78`](#insn-00accb78) → [`00accb7c`](#insn-00accb7c)
- ブロック [`00accb7c`](#insn-00accb7c) 範囲 `[['00accb7c', '00accb8b']]`
  - `CONDITIONAL_JUMP` [`00accb88`](#insn-00accb88) → [`00accb9c`](#insn-00accb9c)
  - `FALL_THROUGH` [`00accb88`](#insn-00accb88) → [`00accb8c`](#insn-00accb8c)
- ブロック [`00accb8c`](#insn-00accb8c) 範囲 `[['00accb8c', '00accb9b']]`
- ブロック [`00accb9c`](#insn-00accb9c) 範囲 `[['00accb9c', '00accbbf']]`

## 命令位置別の参照

- [`00accaec`](#insn-00accaec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accaf0`](#insn-00accaf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accaf4`](#insn-00accaf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accb0c`](#insn-00accb0c) → `00c8e960`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00accb10`](#insn-00accb10) → [`00accb74`](#insn-00accb74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accb20`](#insn-00accb20) → [`00accb34`](#insn-00accb34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accb24`](#insn-00accb24) → [`00accb6c`](#insn-00accb6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accb30`](#insn-00accb30) → [`00accb68`](#insn-00accb68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accb38`](#insn-00accb38) → [`00accb28`](#insn-00accb28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accb44`](#insn-00accb44) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`00accb48`](#insn-00accb48) → [`00accb28`](#insn-00accb28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accb60`](#insn-00accb60) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`00accb64`](#insn-00accb64) → [`00accb28`](#insn-00accb28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accb70`](#insn-00accb70) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00accb78`](#insn-00accb78) → [`00accb8c`](#insn-00accb8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accb84`](#insn-00accb84) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`00accb88`](#insn-00accb88) → [`00accb9c`](#insn-00accb9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accb8c`](#insn-00accb8c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accb90`](#insn-00accb90) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accb94`](#insn-00accb94) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accbb0`](#insn-00accbb0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accbb4`](#insn-00accbb4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accbb8`](#insn-00accbb8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accbbc`](#insn-00accbbc) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00accaec`](#insn-00accaec)

~~~json
{
  "source": "00accaec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accaf0`](#insn-00accaf0)

~~~json
{
  "source": "00accaf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accaf4`](#insn-00accaf4)

~~~json
{
  "source": "00accaf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accb0c`](#insn-00accb0c)

~~~json
{
  "source": "00accb0c",
  "target": "00c8e960",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8e960",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00accb10`](#insn-00accb10)

~~~json
{
  "source": "00accb10",
  "target": "00accb74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accb20`](#insn-00accb20)

~~~json
{
  "source": "00accb20",
  "target": "00accb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accb24`](#insn-00accb24)

~~~json
{
  "source": "00accb24",
  "target": "00accb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accb30`](#insn-00accb30)

~~~json
{
  "source": "00accb30",
  "target": "00accb68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accb38`](#insn-00accb38)

~~~json
{
  "source": "00accb38",
  "target": "00accb28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accb44`](#insn-00accb44)

~~~json
{
  "source": "00accb44",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00accb48`](#insn-00accb48)

~~~json
{
  "source": "00accb48",
  "target": "00accb28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accb60`](#insn-00accb60)

~~~json
{
  "source": "00accb60",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00accb64`](#insn-00accb64)

~~~json
{
  "source": "00accb64",
  "target": "00accb28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accb70`](#insn-00accb70)

~~~json
{
  "source": "00accb70",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00accb78`](#insn-00accb78)

~~~json
{
  "source": "00accb78",
  "target": "00accb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accb84`](#insn-00accb84)

~~~json
{
  "source": "00accb84",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00accb88`](#insn-00accb88)

~~~json
{
  "source": "00accb88",
  "target": "00accb9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accb8c`](#insn-00accb8c)

~~~json
{
  "source": "00accb8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accb90`](#insn-00accb90)

~~~json
{
  "source": "00accb90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accb94`](#insn-00accb94)

~~~json
{
  "source": "00accb94",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accbb0`](#insn-00accbb0)

~~~json
{
  "source": "00accbb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accbb4`](#insn-00accbb4)

~~~json
{
  "source": "00accbb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accbb8`](#insn-00accbb8)

~~~json
{
  "source": "00accbb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accbbc`](#insn-00accbbc)

~~~json
{
  "source": "00accbbc",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
