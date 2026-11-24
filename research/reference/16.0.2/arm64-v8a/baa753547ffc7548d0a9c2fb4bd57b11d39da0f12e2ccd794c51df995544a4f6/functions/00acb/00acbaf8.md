# 00acbaf8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acba88`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acba88.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-52e62eee157a61b44edd9b869de088ef)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00accaec`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00accaec.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-1fe077051b4208b35b07a2a3bcb74a1d)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbaf8",
  "name": "FUN_00acbaf8",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2512a58ea2d267998fb5ca3a8e5a12c69edc909918dd513010f0184c4314ced0",
  "source_text_sha256": "2512a58ea2d267998fb5ca3a8e5a12c69edc909918dd513010f0184c4314ced0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbaf8",
        "00acbbcb"
      ]
    ],
    "bytes_sha256": "d6e0a9131398bff558a41b8b486b5935ed87dda1b1f257aef7bf9d0ab600a052",
    "instruction_count": 53,
    "instruction_bytes": 212,
    "body_bytes": 212,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00731fc4](../00731/00731fc4.md)
- [00732020](../00732/00732020.md)
- [009359a4](../00935/009359a4.md)
- [00935a30](../00935/00935a30.md)
- [00acc088](../00acc/00acc088.md)
- [00acc0e8](../00acc/00acc0e8.md)

## 呼び出し先

- [00c53da0](../00c53/00c53da0.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57f80](../00c57/00c57f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1049 bytes

~~~c

void FUN_00acbaf8(undefined8 *param_1)

{
  void *__ptr;
  long lVar1;
  long *plVar2;
  void *pvVar3;
  void *pvVar4;
  
  pvVar3 = (void *)param_1[8];
  *param_1 = &PTR_FUN_00c8d990;
  if (pvVar3 != (void *)0x0) {
    pvVar4 = (void *)param_1[9];
    __ptr = pvVar3;
    if (pvVar4 != pvVar3) {
      do {
        plVar2 = *(long **)((long)pvVar4 + -8);
        if ((plVar2 != (long *)0x0) &&
           (lVar1 = FUN_00c53da0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0)) {
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
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53da0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
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
<a id="insn-00acbaf8"></a> `00acbaf8` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00acbafc"></a> `00acbafc` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbb00"></a> `00acbb00` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbb04"></a> `00acbb04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acbb08"></a> `00acbb08` | `15 20 40 f9` | ldr x21,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00acbb0c"></a> `00acbb0c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acbb10"></a> `00acbb10` | `08 0e 00 d0` | adrp x8,0xc8d000 | `FALL_THROUGH`
<a id="insn-00acbb14"></a> `00acbb14` | `08 41 26 91` | add x8,x8,#0x990 | `FALL_THROUGH`
<a id="insn-00acbb18"></a> `00acbb18` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00acbb1c"></a> `00acbb1c` | `35 03 00 b4` | cbz x21,0x00acbb80 | `CONDITIONAL_JUMP`
<a id="insn-00acbb20"></a> `00acbb20` | `76 26 40 f9` | ldr x22,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00acbb24"></a> `00acbb24` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acbb28"></a> `00acbb28` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-00acbb2c"></a> `00acbb2c` | `a1 00 00 54` | b.ne 0x00acbb40 | `CONDITIONAL_JUMP`
<a id="insn-00acbb30"></a> `00acbb30` | `12 00 00 14` | b 0x00acbb78 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbb34"></a> `00acbb34` | `d6 42 00 d1` | sub x22,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00acbb38"></a> `00acbb38` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-00acbb3c"></a> `00acbb3c` | `c0 01 00 54` | b.eq 0x00acbb74 | `CONDITIONAL_JUMP`
<a id="insn-00acbb40"></a> `00acbb40` | `d4 82 5f f8` | ldur x20,[x22, #-0x8] | `FALL_THROUGH`
<a id="insn-00acbb44"></a> `00acbb44` | `94 ff ff b4` | cbz x20,0x00acbb34 | `CONDITIONAL_JUMP`
<a id="insn-00acbb48"></a> `00acbb48` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acbb4c"></a> `00acbb4c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acbb50"></a> `00acbb50` | `94 20 06 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-00acbb54"></a> `00acbb54` | `00 ff ff b5` | cbnz x0,0x00acbb34 | `CONDITIONAL_JUMP`
<a id="insn-00acbb58"></a> `00acbb58` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00acbb5c"></a> `00acbb5c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acbb60"></a> `00acbb60` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acbb64"></a> `00acbb64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbb68"></a> `00acbb68` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acbb6c"></a> `00acbb6c` | `f9 30 06 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-00acbb70"></a> `00acbb70` | `f1 ff ff 17` | b 0x00acbb34 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbb74"></a> `00acbb74` | `60 22 40 f9` | ldr x0,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00acbb78"></a> `00acbb78` | `75 26 00 f9` | str x21,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00acbb7c"></a> `00acbb7c` | `01 31 06 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00acbb80"></a> `00acbb80` | `73 1e 40 f9` | ldr x19,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00acbb84"></a> `00acbb84` | `b3 00 00 b4` | cbz x19,0x00acbb98 | `CONDITIONAL_JUMP`
<a id="insn-00acbb88"></a> `00acbb88` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00acbb8c"></a> `00acbb8c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acbb90"></a> `00acbb90` | `84 20 06 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-00acbb94"></a> `00acbb94` | `a0 00 00 b4` | cbz x0,0x00acbba8 | `CONDITIONAL_JUMP`
<a id="insn-00acbb98"></a> `00acbb98` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbb9c"></a> `00acbb9c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbba0"></a> `00acbba0` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00acbba4"></a> `00acbba4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acbba8"></a> `00acbba8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00acbbac"></a> `00acbbac` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acbbb0"></a> `00acbbb0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acbbb4"></a> `00acbbb4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbbb8"></a> `00acbbb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acbbbc"></a> `00acbbbc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbbc0"></a> `00acbbc0` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbbc4"></a> `00acbbc4` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00acbbc8"></a> `00acbbc8` | `e2 30 06 14` | b 0x00c57f50 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbaf8`](#insn-00acbaf8) 範囲 `[['00acbaf8', '00acbb1f']]`
  - `CONDITIONAL_JUMP` [`00acbb1c`](#insn-00acbb1c) → [`00acbb80`](#insn-00acbb80)
  - `FALL_THROUGH` [`00acbb1c`](#insn-00acbb1c) → [`00acbb20`](#insn-00acbb20)
- ブロック [`00acbb20`](#insn-00acbb20) 範囲 `[['00acbb20', '00acbb2f']]`
  - `CONDITIONAL_JUMP` [`00acbb2c`](#insn-00acbb2c) → [`00acbb40`](#insn-00acbb40)
  - `FALL_THROUGH` [`00acbb2c`](#insn-00acbb2c) → [`00acbb30`](#insn-00acbb30)
- ブロック [`00acbb30`](#insn-00acbb30) 範囲 `[['00acbb30', '00acbb33']]`
  - `UNCONDITIONAL_JUMP` [`00acbb30`](#insn-00acbb30) → [`00acbb78`](#insn-00acbb78)
- ブロック [`00acbb34`](#insn-00acbb34) 範囲 `[['00acbb34', '00acbb3f']]`
  - `CONDITIONAL_JUMP` [`00acbb3c`](#insn-00acbb3c) → [`00acbb74`](#insn-00acbb74)
  - `FALL_THROUGH` [`00acbb3c`](#insn-00acbb3c) → [`00acbb40`](#insn-00acbb40)
- ブロック [`00acbb40`](#insn-00acbb40) 範囲 `[['00acbb40', '00acbb47']]`
  - `CONDITIONAL_JUMP` [`00acbb44`](#insn-00acbb44) → [`00acbb34`](#insn-00acbb34)
  - `FALL_THROUGH` [`00acbb44`](#insn-00acbb44) → [`00acbb48`](#insn-00acbb48)
- ブロック [`00acbb48`](#insn-00acbb48) 範囲 `[['00acbb48', '00acbb57']]`
  - `CONDITIONAL_JUMP` [`00acbb54`](#insn-00acbb54) → [`00acbb34`](#insn-00acbb34)
  - `FALL_THROUGH` [`00acbb54`](#insn-00acbb54) → [`00acbb58`](#insn-00acbb58)
- ブロック [`00acbb58`](#insn-00acbb58) 範囲 `[['00acbb58', '00acbb73']]`
  - `UNCONDITIONAL_JUMP` [`00acbb70`](#insn-00acbb70) → [`00acbb34`](#insn-00acbb34)
- ブロック [`00acbb74`](#insn-00acbb74) 範囲 `[['00acbb74', '00acbb77']]`
  - `FALL_THROUGH` [`00acbb74`](#insn-00acbb74) → [`00acbb78`](#insn-00acbb78)
- ブロック [`00acbb78`](#insn-00acbb78) 範囲 `[['00acbb78', '00acbb7f']]`
  - `FALL_THROUGH` [`00acbb7c`](#insn-00acbb7c) → [`00acbb80`](#insn-00acbb80)
- ブロック [`00acbb80`](#insn-00acbb80) 範囲 `[['00acbb80', '00acbb87']]`
  - `CONDITIONAL_JUMP` [`00acbb84`](#insn-00acbb84) → [`00acbb98`](#insn-00acbb98)
  - `FALL_THROUGH` [`00acbb84`](#insn-00acbb84) → [`00acbb88`](#insn-00acbb88)
- ブロック [`00acbb88`](#insn-00acbb88) 範囲 `[['00acbb88', '00acbb97']]`
  - `CONDITIONAL_JUMP` [`00acbb94`](#insn-00acbb94) → [`00acbba8`](#insn-00acbba8)
  - `FALL_THROUGH` [`00acbb94`](#insn-00acbb94) → [`00acbb98`](#insn-00acbb98)
- ブロック [`00acbb98`](#insn-00acbb98) 範囲 `[['00acbb98', '00acbba7']]`
- ブロック [`00acbba8`](#insn-00acbba8) 範囲 `[['00acbba8', '00acbbcb']]`

## 命令位置別の参照

- [`00acbaf8`](#insn-00acbaf8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbafc`](#insn-00acbafc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb00`](#insn-00acbb00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb18`](#insn-00acbb18) → `00c8d990`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acbb1c`](#insn-00acbb1c) → [`00acbb80`](#insn-00acbb80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb2c`](#insn-00acbb2c) → [`00acbb40`](#insn-00acbb40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb30`](#insn-00acbb30) → [`00acbb78`](#insn-00acbb78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb3c`](#insn-00acbb3c) → [`00acbb74`](#insn-00acbb74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb44`](#insn-00acbb44) → [`00acbb34`](#insn-00acbb34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb50`](#insn-00acbb50) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`00acbb54`](#insn-00acbb54) → [`00acbb34`](#insn-00acbb34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb6c`](#insn-00acbb6c) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`00acbb70`](#insn-00acbb70) → [`00acbb34`](#insn-00acbb34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb7c`](#insn-00acbb7c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00acbb84`](#insn-00acbb84) → [`00acbb98`](#insn-00acbb98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb90`](#insn-00acbb90) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`00acbb94`](#insn-00acbb94) → [`00acbba8`](#insn-00acbba8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb98`](#insn-00acbb98) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb9c`](#insn-00acbb9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbba0`](#insn-00acbba0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbbc`](#insn-00acbbbc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbc0`](#insn-00acbbc0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbc4`](#insn-00acbbc4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbc8`](#insn-00acbbc8) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbaf8`](#insn-00acbaf8)

~~~json
{
  "source": "00acbaf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbafc`](#insn-00acbafc)

~~~json
{
  "source": "00acbafc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb00`](#insn-00acbb00)

~~~json
{
  "source": "00acbb00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb18`](#insn-00acbb18)

~~~json
{
  "source": "00acbb18",
  "target": "00c8d990",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d990",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acbb1c`](#insn-00acbb1c)

~~~json
{
  "source": "00acbb1c",
  "target": "00acbb80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb2c`](#insn-00acbb2c)

~~~json
{
  "source": "00acbb2c",
  "target": "00acbb40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb30`](#insn-00acbb30)

~~~json
{
  "source": "00acbb30",
  "target": "00acbb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb3c`](#insn-00acbb3c)

~~~json
{
  "source": "00acbb3c",
  "target": "00acbb74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb44`](#insn-00acbb44)

~~~json
{
  "source": "00acbb44",
  "target": "00acbb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb50`](#insn-00acbb50)

~~~json
{
  "source": "00acbb50",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbb54`](#insn-00acbb54)

~~~json
{
  "source": "00acbb54",
  "target": "00acbb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb6c`](#insn-00acbb6c)

~~~json
{
  "source": "00acbb6c",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbb70`](#insn-00acbb70)

~~~json
{
  "source": "00acbb70",
  "target": "00acbb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb7c`](#insn-00acbb7c)

~~~json
{
  "source": "00acbb7c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbb84`](#insn-00acbb84)

~~~json
{
  "source": "00acbb84",
  "target": "00acbb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb90`](#insn-00acbb90)

~~~json
{
  "source": "00acbb90",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbb94`](#insn-00acbb94)

~~~json
{
  "source": "00acbb94",
  "target": "00acbba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb98`](#insn-00acbb98)

~~~json
{
  "source": "00acbb98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb9c`](#insn-00acbb9c)

~~~json
{
  "source": "00acbb9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbba0`](#insn-00acbba0)

~~~json
{
  "source": "00acbba0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbbc`](#insn-00acbbbc)

~~~json
{
  "source": "00acbbbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbc0`](#insn-00acbbc0)

~~~json
{
  "source": "00acbbc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbc4`](#insn-00acbbc4)

~~~json
{
  "source": "00acbbc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbc8`](#insn-00acbbc8)

~~~json
{
  "source": "00acbbc8",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
