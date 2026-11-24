# 00acfbe0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00acf9e4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf9e4.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-a4e512e2f1b0497e6109259d57b0f7c2)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acfc50`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acfc50.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-6ba3e8da4e9acad263901a8be78500ec)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acfbe0",
  "name": "FUN_00acfbe0",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e36702f0cc624eafcfcb49211d5ad2d1008ff6bcd4db08ce8471aac63fd540d2",
  "source_text_sha256": "e36702f0cc624eafcfcb49211d5ad2d1008ff6bcd4db08ce8471aac63fd540d2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acfbe0",
        "00acfcbf"
      ]
    ],
    "bytes_sha256": "d80ccc1a0e2fbc83e00df60010836b8e92b10281648d4cede17433631876ef2a",
    "instruction_count": 56,
    "instruction_bytes": 224,
    "body_bytes": 224,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00ad6f4c](../00ad6/00ad6f4c.md)

## 呼び出し先

- [00695bac](../00695/00695bac.md)
- [009a2b34](../009a2/009a2b34.md)
- [00c53cd0](../00c53/00c53cd0.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1110 bytes

~~~c

void FUN_00acfbe0(long param_1,undefined4 param_2,long *param_3)

{
  long lVar1;
  long lVar2;
  long lVar3;
  long lVar4;
  long *plVar5;
  undefined4 local_58;
  undefined1 uStack_51;
  undefined4 *local_50;
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  local_58 = param_2;
  if (*param_3 == 0) {
    FUN_009a2b34(param_1 + 0x318,&local_58);
  }
  else {
    local_50 = &local_58;
    lVar3 = FUN_00695bac(param_1 + 0x318,&local_58,&DAT_002c86f5,&local_50,&uStack_51);
    lVar4 = *param_3;
    lVar1 = param_3[1];
    if (lVar1 != 0) {
      FUN_00c53cd0(1,lVar1 + 8);
    }
    plVar5 = *(long **)(lVar3 + 0x20);
    *(long *)(lVar3 + 0x18) = lVar4;
    *(long *)(lVar3 + 0x20) = lVar1;
    if ((plVar5 != (long *)0x0) && (lVar4 = FUN_00c53d00(0xffffffffffffffff,plVar5 + 1), lVar4 == 0)
       ) {
      (**(code **)(*plVar5 + 0x10))(plVar5);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar5);
    }
  }
  if (*(long *)(lVar2 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acfbe0"></a> `00acfbe0` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acfbe4"></a> `00acfbe4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acfbe8"></a> `00acfbe8` | `f7 1b 00 f9` | str x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acfbec"></a> `00acfbec` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acfbf0"></a> `00acfbf0` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acfbf4"></a> `00acfbf4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00acfbf8"></a> `00acfbf8` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acfbfc"></a> `00acfbfc` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acfc00"></a> `00acfc00` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acfc04"></a> `00acfc04` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00acfc08"></a> `00acfc08` | `e1 0b 00 b9` | str w1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acfc0c"></a> `00acfc0c` | `e8 03 00 b4` | cbz x8,0x00acfc88 | `CONDITIONAL_JUMP`
<a id="insn-00acfc10"></a> `00acfc10` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00acfc14"></a> `00acfc14` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00acfc18"></a> `00acfc18` | `c2 bf ff b0` | adrp x2,0x2c8000 | `FALL_THROUGH`
<a id="insn-00acfc1c"></a> `00acfc1c` | `42 d4 1b 91` | add x2,x2,#0x6f5 | `FALL_THROUGH`
<a id="insn-00acfc20"></a> `00acfc20` | `00 60 0c 91` | add x0,x0,#0x318 | `FALL_THROUGH`
<a id="insn-00acfc24"></a> `00acfc24` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00acfc28"></a> `00acfc28` | `e3 43 00 91` | add x3,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00acfc2c"></a> `00acfc2c` | `e4 3f 00 91` | add x4,sp,#0xf | `FALL_THROUGH`
<a id="insn-00acfc30"></a> `00acfc30` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfc34"></a> `00acfc34` | `de 17 ef 97` | bl 0x00695bac | `UNCONDITIONAL_CALL`
<a id="insn-00acfc38"></a> `00acfc38` | `77 5a 40 a9` | ldp x23,x22,[x19] | `FALL_THROUGH`
<a id="insn-00acfc3c"></a> `00acfc3c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acfc40"></a> `00acfc40` | `96 00 00 b4` | cbz x22,0x00acfc50 | `CONDITIONAL_JUMP`
<a id="insn-00acfc44"></a> `00acfc44` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00acfc48"></a> `00acfc48` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00acfc4c"></a> `00acfc4c` | `21 10 06 94` | bl 0x00c53cd0 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc50"></a> `00acfc50` | `93 12 40 f9` | ldr x19,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acfc54"></a> `00acfc54` | `97 da 01 a9` | stp x23,x22,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00acfc58"></a> `00acfc58` | `f3 01 00 b4` | cbz x19,0x00acfc94 | `CONDITIONAL_JUMP`
<a id="insn-00acfc5c"></a> `00acfc5c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00acfc60"></a> `00acfc60` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acfc64"></a> `00acfc64` | `27 10 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc68"></a> `00acfc68` | `60 01 00 b5` | cbnz x0,0x00acfc94 | `CONDITIONAL_JUMP`
<a id="insn-00acfc6c"></a> `00acfc6c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00acfc70"></a> `00acfc70` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acfc74"></a> `00acfc74` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acfc78"></a> `00acfc78` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acfc7c"></a> `00acfc7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acfc80"></a> `00acfc80` | `80 20 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc84"></a> `00acfc84` | `04 00 00 14` | b 0x00acfc94 | `UNCONDITIONAL_JUMP`
<a id="insn-00acfc88"></a> `00acfc88` | `00 60 0c 91` | add x0,x0,#0x318 | `FALL_THROUGH`
<a id="insn-00acfc8c"></a> `00acfc8c` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00acfc90"></a> `00acfc90` | `a9 4b fb 97` | bl 0x009a2b34 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc94"></a> `00acfc94` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acfc98"></a> `00acfc98` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acfc9c"></a> `00acfc9c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acfca0"></a> `00acfca0` | `e1 00 00 54` | b.ne 0x00acfcbc | `CONDITIONAL_JUMP`
<a id="insn-00acfca4"></a> `00acfca4` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acfca8"></a> `00acfca8` | `f7 1b 40 f9` | ldr x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acfcac"></a> `00acfcac` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acfcb0"></a> `00acfcb0` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acfcb4"></a> `00acfcb4` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acfcb8"></a> `00acfcb8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acfcbc"></a> `00acfcbc` | `89 20 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acfbe0`](#insn-00acfbe0) 範囲 `[['00acfbe0', '00acfc0f']]`
  - `CONDITIONAL_JUMP` [`00acfc0c`](#insn-00acfc0c) → [`00acfc88`](#insn-00acfc88)
  - `FALL_THROUGH` [`00acfc0c`](#insn-00acfc0c) → [`00acfc10`](#insn-00acfc10)
- ブロック [`00acfc10`](#insn-00acfc10) 範囲 `[['00acfc10', '00acfc43']]`
  - `CONDITIONAL_JUMP` [`00acfc40`](#insn-00acfc40) → [`00acfc50`](#insn-00acfc50)
  - `FALL_THROUGH` [`00acfc40`](#insn-00acfc40) → [`00acfc44`](#insn-00acfc44)
- ブロック [`00acfc44`](#insn-00acfc44) 範囲 `[['00acfc44', '00acfc4f']]`
  - `FALL_THROUGH` [`00acfc4c`](#insn-00acfc4c) → [`00acfc50`](#insn-00acfc50)
- ブロック [`00acfc50`](#insn-00acfc50) 範囲 `[['00acfc50', '00acfc5b']]`
  - `CONDITIONAL_JUMP` [`00acfc58`](#insn-00acfc58) → [`00acfc94`](#insn-00acfc94)
  - `FALL_THROUGH` [`00acfc58`](#insn-00acfc58) → [`00acfc5c`](#insn-00acfc5c)
- ブロック [`00acfc5c`](#insn-00acfc5c) 範囲 `[['00acfc5c', '00acfc6b']]`
  - `CONDITIONAL_JUMP` [`00acfc68`](#insn-00acfc68) → [`00acfc94`](#insn-00acfc94)
  - `FALL_THROUGH` [`00acfc68`](#insn-00acfc68) → [`00acfc6c`](#insn-00acfc6c)
- ブロック [`00acfc6c`](#insn-00acfc6c) 範囲 `[['00acfc6c', '00acfc87']]`
  - `UNCONDITIONAL_JUMP` [`00acfc84`](#insn-00acfc84) → [`00acfc94`](#insn-00acfc94)
- ブロック [`00acfc88`](#insn-00acfc88) 範囲 `[['00acfc88', '00acfc93']]`
  - `FALL_THROUGH` [`00acfc90`](#insn-00acfc90) → [`00acfc94`](#insn-00acfc94)
- ブロック [`00acfc94`](#insn-00acfc94) 範囲 `[['00acfc94', '00acfca3']]`
  - `CONDITIONAL_JUMP` [`00acfca0`](#insn-00acfca0) → [`00acfcbc`](#insn-00acfcbc)
  - `FALL_THROUGH` [`00acfca0`](#insn-00acfca0) → [`00acfca4`](#insn-00acfca4)
- ブロック [`00acfca4`](#insn-00acfca4) 範囲 `[['00acfca4', '00acfcbb']]`
- ブロック [`00acfcbc`](#insn-00acfcbc) 範囲 `[['00acfcbc', '00acfcbf']]`

## 命令位置別の参照

- [`00acfbe4`](#insn-00acfbe4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbe8`](#insn-00acfbe8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbec`](#insn-00acfbec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbf0`](#insn-00acfbf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc00`](#insn-00acfc00) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc08`](#insn-00acfc08) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc0c`](#insn-00acfc0c) → [`00acfc88`](#insn-00acfc88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc1c`](#insn-00acfc1c) → `002c86f5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc30`](#insn-00acfc30) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc34`](#insn-00acfc34) → [`00695bac`](../00695/00695bac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00695bac` · 推定シンボル `None` · 推定型 `None`
- [`00acfc40`](#insn-00acfc40) → [`00acfc50`](#insn-00acfc50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc4c`](#insn-00acfc4c) → [`00c53cd0`](../00c53/00c53cd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53cd0` · 推定シンボル `None` · 推定型 `None`
- [`00acfc58`](#insn-00acfc58) → [`00acfc94`](#insn-00acfc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc64`](#insn-00acfc64) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00acfc68`](#insn-00acfc68) → [`00acfc94`](#insn-00acfc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc80`](#insn-00acfc80) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00acfc84`](#insn-00acfc84) → [`00acfc94`](#insn-00acfc94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc90`](#insn-00acfc90) → [`009a2b34`](../009a2/009a2b34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009a2b34` · 推定シンボル `None` · 推定型 `None`
- [`00acfc98`](#insn-00acfc98) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfca0`](#insn-00acfca0) → [`00acfcbc`](#insn-00acfcbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfca4`](#insn-00acfca4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfca8`](#insn-00acfca8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcac`](#insn-00acfcac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcb0`](#insn-00acfcb0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcbc`](#insn-00acfcbc) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acfbe4`](#insn-00acfbe4)

~~~json
{
  "source": "00acfbe4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbe8`](#insn-00acfbe8)

~~~json
{
  "source": "00acfbe8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbec`](#insn-00acfbec)

~~~json
{
  "source": "00acfbec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbf0`](#insn-00acfbf0)

~~~json
{
  "source": "00acfbf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc00`](#insn-00acfc00)

~~~json
{
  "source": "00acfc00",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc08`](#insn-00acfc08)

~~~json
{
  "source": "00acfc08",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc0c`](#insn-00acfc0c)

~~~json
{
  "source": "00acfc0c",
  "target": "00acfc88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc1c`](#insn-00acfc1c)

~~~json
{
  "source": "00acfc1c",
  "target": "002c86f5",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc30`](#insn-00acfc30)

~~~json
{
  "source": "00acfc30",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc34`](#insn-00acfc34)

~~~json
{
  "source": "00acfc34",
  "target": "00695bac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc40`](#insn-00acfc40)

~~~json
{
  "source": "00acfc40",
  "target": "00acfc50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc4c`](#insn-00acfc4c)

~~~json
{
  "source": "00acfc4c",
  "target": "00c53cd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc58`](#insn-00acfc58)

~~~json
{
  "source": "00acfc58",
  "target": "00acfc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc64`](#insn-00acfc64)

~~~json
{
  "source": "00acfc64",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc68`](#insn-00acfc68)

~~~json
{
  "source": "00acfc68",
  "target": "00acfc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc80`](#insn-00acfc80)

~~~json
{
  "source": "00acfc80",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc84`](#insn-00acfc84)

~~~json
{
  "source": "00acfc84",
  "target": "00acfc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc90`](#insn-00acfc90)

~~~json
{
  "source": "00acfc90",
  "target": "009a2b34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc98`](#insn-00acfc98)

~~~json
{
  "source": "00acfc98",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfca0`](#insn-00acfca0)

~~~json
{
  "source": "00acfca0",
  "target": "00acfcbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfca4`](#insn-00acfca4)

~~~json
{
  "source": "00acfca4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfca8`](#insn-00acfca8)

~~~json
{
  "source": "00acfca8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcac`](#insn-00acfcac)

~~~json
{
  "source": "00acfcac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcb0`](#insn-00acfcb0)

~~~json
{
  "source": "00acfcb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcbc`](#insn-00acfcbc)

~~~json
{
  "source": "00acfcbc",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
