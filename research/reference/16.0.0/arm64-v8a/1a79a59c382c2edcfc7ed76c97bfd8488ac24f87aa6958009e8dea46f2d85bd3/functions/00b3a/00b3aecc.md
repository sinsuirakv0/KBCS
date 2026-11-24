# 00b3aecc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0019.md#review-45ed88581639dd691e3c6ce3d2fbb23b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b3b2f4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3b2f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0007.md#compare-4a1f96db9cf73e9f9a066810f8146d93)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b3aecc",
  "name": "FUN_00b3aecc",
  "size": 220,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1295c6866fdc571deadc25eac4126a8c56105f08bafabed28aaf90ff60069162",
  "source_text_sha256": "1295c6866fdc571deadc25eac4126a8c56105f08bafabed28aaf90ff60069162",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b3aecc",
        "00b3afa7"
      ]
    ],
    "bytes_sha256": "53e5bf603f9d25add2c57e379a0a52d3d2e85f9094dab42bfb0f3df671006ed6",
    "instruction_count": 55,
    "instruction_bytes": 220,
    "body_bytes": 220,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1586 bytes

~~~c

void FUN_00b3aecc(undefined8 *param_1,undefined8 param_2)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  void *__ptr;
  
  __ptr = (void *)*param_1;
  *param_1 = param_2;
  if (__ptr == (void *)0x0) {
    return;
  }
  if (*(char *)(param_1 + 2) == '\0') goto LAB_00b3af98;
  plVar1 = *(long **)((long)__ptr + 0xc0);
  plVar3 = (long *)((long)__ptr + 0xa0);
  if (plVar1 == plVar3) {
    lVar4 = 0x20;
LAB_00b3af1c:
    (**(code **)(*plVar3 + lVar4))();
  }
  else if (plVar1 != (long *)0x0) {
    lVar4 = 0x28;
    plVar3 = plVar1;
    goto LAB_00b3af1c;
  }
  plVar2 = *(long **)((long)__ptr + 0x90);
  plVar3 = (long *)((long)__ptr + 0x70);
  plVar1 = (long *)((long)__ptr + 0x40);
                    /* try { // try from 00b3af34 to 00c3af3b has its CatchHandler @ 00b3b60c */
  if (plVar2 == plVar3) {
    lVar4 = 0x20;
LAB_00b3af50:
    (**(code **)(*plVar3 + lVar4))();
  }
  else if (plVar2 != (long *)0x0) {
    lVar4 = 0x28;
    plVar3 = plVar2;
    goto LAB_00b3af50;
  }
  plVar3 = *(long **)((long)__ptr + 0x60);
  if (plVar3 == plVar1) {
    lVar4 = 0x20;
LAB_00b3af7c:
                    /* try { // try from 00b3af84 to 00c3af97 has its CatchHandler @ 00b3b5d8 */
    (**(code **)(*plVar1 + lVar4))();
  }
  else if (plVar3 != (long *)0x0) {
                    /* try { // try from 00b3af6c to 00c3af83 has its CatchHandler @ 00b3b5f0 */
    lVar4 = 0x28;
    plVar1 = plVar3;
    goto LAB_00b3af7c;
  }
  if ((*(byte *)((long)__ptr + 0x20) & 1) != 0) {
    _ZdlPv(*(void **)((long)__ptr + 0x30));
  }
LAB_00b3af98:
  _ZdlPv(__ptr);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b3aecc"></a> `00b3aecc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b3aed0"></a> `00b3aed0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3aed4"></a> `00b3aed4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b3aed8"></a> `00b3aed8` | `13 00 40 f9` | ldr x19,[x0] | `FALL_THROUGH`
<a id="insn-00b3aedc"></a> `00b3aedc` | `01 00 00 f9` | str x1,[x0] | `FALL_THROUGH`
<a id="insn-00b3aee0"></a> `00b3aee0` | `53 01 00 b4` | cbz x19,0x00b3af08 | `CONDITIONAL_JUMP`
<a id="insn-00b3aee4"></a> `00b3aee4` | `08 40 40 39` | ldrb w8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b3aee8"></a> `00b3aee8` | `88 05 00 34` | cbz w8,0x00b3af98 | `CONDITIONAL_JUMP`
<a id="insn-00b3aeec"></a> `00b3aeec` | `60 62 40 f9` | ldr x0,[x19, #0xc0] | `FALL_THROUGH`
<a id="insn-00b3aef0"></a> `00b3aef0` | `69 82 02 91` | add x9,x19,#0xa0 | `FALL_THROUGH`
<a id="insn-00b3aef4"></a> `00b3aef4` | `1f 00 09 eb` | cmp x0,x9 | `FALL_THROUGH`
<a id="insn-00b3aef8"></a> `00b3aef8` | `e0 00 00 54` | b.eq 0x00b3af14 | `CONDITIONAL_JUMP`
<a id="insn-00b3aefc"></a> `00b3aefc` | `60 01 00 b4` | cbz x0,0x00b3af28 | `CONDITIONAL_JUMP`
<a id="insn-00b3af00"></a> `00b3af00` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00b3af04"></a> `00b3af04` | `06 00 00 14` | b 0x00b3af1c | `UNCONDITIONAL_JUMP`
<a id="insn-00b3af08"></a> `00b3af08` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3af0c"></a> `00b3af0c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b3af10"></a> `00b3af10` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b3af14"></a> `00b3af14` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00b3af18"></a> `00b3af18` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00b3af1c"></a> `00b3af1c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00b3af20"></a> `00b3af20` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b3af24"></a> `00b3af24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b3af28"></a> `00b3af28` | `60 4a 40 f9` | ldr x0,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00b3af2c"></a> `00b3af2c` | `69 c2 01 91` | add x9,x19,#0x70 | `FALL_THROUGH`
<a id="insn-00b3af30"></a> `00b3af30` | `74 02 01 91` | add x20,x19,#0x40 | `FALL_THROUGH`
<a id="insn-00b3af34"></a> `00b3af34` | `1f 00 09 eb` | cmp x0,x9 | `FALL_THROUGH`
<a id="insn-00b3af38"></a> `00b3af38` | `80 00 00 54` | b.eq 0x00b3af48 | `CONDITIONAL_JUMP`
<a id="insn-00b3af3c"></a> `00b3af3c` | `00 01 00 b4` | cbz x0,0x00b3af5c | `CONDITIONAL_JUMP`
<a id="insn-00b3af40"></a> `00b3af40` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00b3af44"></a> `00b3af44` | `03 00 00 14` | b 0x00b3af50 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3af48"></a> `00b3af48` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00b3af4c"></a> `00b3af4c` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00b3af50"></a> `00b3af50` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00b3af54"></a> `00b3af54` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b3af58"></a> `00b3af58` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b3af5c"></a> `00b3af5c` | `60 32 40 f9` | ldr x0,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00b3af60"></a> `00b3af60` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-00b3af64"></a> `00b3af64` | `80 00 00 54` | b.eq 0x00b3af74 | `CONDITIONAL_JUMP`
<a id="insn-00b3af68"></a> `00b3af68` | `00 01 00 b4` | cbz x0,0x00b3af88 | `CONDITIONAL_JUMP`
<a id="insn-00b3af6c"></a> `00b3af6c` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00b3af70"></a> `00b3af70` | `03 00 00 14` | b 0x00b3af7c | `UNCONDITIONAL_JUMP`
<a id="insn-00b3af74"></a> `00b3af74` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00b3af78"></a> `00b3af78` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b3af7c"></a> `00b3af7c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00b3af80"></a> `00b3af80` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b3af84"></a> `00b3af84` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b3af88"></a> `00b3af88` | `68 82 40 39` | ldrb w8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00b3af8c"></a> `00b3af8c` | `68 00 00 36` | tbz w8,#0x0,0x00b3af98 | `CONDITIONAL_JUMP`
<a id="insn-00b3af90"></a> `00b3af90` | `60 1a 40 f9` | ldr x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b3af94"></a> `00b3af94` | `c7 72 04 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00b3af98"></a> `00b3af98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b3af9c"></a> `00b3af9c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3afa0"></a> `00b3afa0` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b3afa4"></a> `00b3afa4` | `c3 72 04 14` | b 0x00c57ab0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b3aecc`](#insn-00b3aecc) 範囲 `[['00b3aecc', '00b3aee3']]`
  - `CONDITIONAL_JUMP` [`00b3aee0`](#insn-00b3aee0) → [`00b3af08`](#insn-00b3af08)
  - `FALL_THROUGH` [`00b3aee0`](#insn-00b3aee0) → [`00b3aee4`](#insn-00b3aee4)
- ブロック [`00b3aee4`](#insn-00b3aee4) 範囲 `[['00b3aee4', '00b3aeeb']]`
  - `CONDITIONAL_JUMP` [`00b3aee8`](#insn-00b3aee8) → [`00b3af98`](#insn-00b3af98)
  - `FALL_THROUGH` [`00b3aee8`](#insn-00b3aee8) → [`00b3aeec`](#insn-00b3aeec)
- ブロック [`00b3aeec`](#insn-00b3aeec) 範囲 `[['00b3aeec', '00b3aefb']]`
  - `CONDITIONAL_JUMP` [`00b3aef8`](#insn-00b3aef8) → [`00b3af14`](#insn-00b3af14)
  - `FALL_THROUGH` [`00b3aef8`](#insn-00b3aef8) → [`00b3aefc`](#insn-00b3aefc)
- ブロック [`00b3aefc`](#insn-00b3aefc) 範囲 `[['00b3aefc', '00b3aeff']]`
  - `CONDITIONAL_JUMP` [`00b3aefc`](#insn-00b3aefc) → [`00b3af28`](#insn-00b3af28)
  - `FALL_THROUGH` [`00b3aefc`](#insn-00b3aefc) → [`00b3af00`](#insn-00b3af00)
- ブロック [`00b3af00`](#insn-00b3af00) 範囲 `[['00b3af00', '00b3af07']]`
  - `UNCONDITIONAL_JUMP` [`00b3af04`](#insn-00b3af04) → [`00b3af1c`](#insn-00b3af1c)
- ブロック [`00b3af08`](#insn-00b3af08) 範囲 `[['00b3af08', '00b3af13']]`
- ブロック [`00b3af14`](#insn-00b3af14) 範囲 `[['00b3af14', '00b3af1b']]`
  - `FALL_THROUGH` [`00b3af18`](#insn-00b3af18) → [`00b3af1c`](#insn-00b3af1c)
- ブロック [`00b3af1c`](#insn-00b3af1c) 範囲 `[['00b3af1c', '00b3af27']]`
  - `FALL_THROUGH` [`00b3af24`](#insn-00b3af24) → [`00b3af28`](#insn-00b3af28)
- ブロック [`00b3af28`](#insn-00b3af28) 範囲 `[['00b3af28', '00b3af33']]`
  - `FALL_THROUGH` [`00b3af30`](#insn-00b3af30) → [`00b3af34`](#insn-00b3af34)
- ブロック [`00b3af34`](#insn-00b3af34) 範囲 `[['00b3af34', '00b3af3b']]`
  - `CONDITIONAL_JUMP` [`00b3af38`](#insn-00b3af38) → [`00b3af48`](#insn-00b3af48)
  - `FALL_THROUGH` [`00b3af38`](#insn-00b3af38) → [`00b3af3c`](#insn-00b3af3c)
- ブロック [`00b3af3c`](#insn-00b3af3c) 範囲 `[['00b3af3c', '00b3af3f']]`
  - `CONDITIONAL_JUMP` [`00b3af3c`](#insn-00b3af3c) → [`00b3af5c`](#insn-00b3af5c)
  - `FALL_THROUGH` [`00b3af3c`](#insn-00b3af3c) → [`00b3af40`](#insn-00b3af40)
- ブロック [`00b3af40`](#insn-00b3af40) 範囲 `[['00b3af40', '00b3af47']]`
  - `UNCONDITIONAL_JUMP` [`00b3af44`](#insn-00b3af44) → [`00b3af50`](#insn-00b3af50)
- ブロック [`00b3af48`](#insn-00b3af48) 範囲 `[['00b3af48', '00b3af4f']]`
  - `FALL_THROUGH` [`00b3af4c`](#insn-00b3af4c) → [`00b3af50`](#insn-00b3af50)
- ブロック [`00b3af50`](#insn-00b3af50) 範囲 `[['00b3af50', '00b3af5b']]`
  - `FALL_THROUGH` [`00b3af58`](#insn-00b3af58) → [`00b3af5c`](#insn-00b3af5c)
- ブロック [`00b3af5c`](#insn-00b3af5c) 範囲 `[['00b3af5c', '00b3af67']]`
  - `CONDITIONAL_JUMP` [`00b3af64`](#insn-00b3af64) → [`00b3af74`](#insn-00b3af74)
  - `FALL_THROUGH` [`00b3af64`](#insn-00b3af64) → [`00b3af68`](#insn-00b3af68)
- ブロック [`00b3af68`](#insn-00b3af68) 範囲 `[['00b3af68', '00b3af6b']]`
  - `CONDITIONAL_JUMP` [`00b3af68`](#insn-00b3af68) → [`00b3af88`](#insn-00b3af88)
  - `FALL_THROUGH` [`00b3af68`](#insn-00b3af68) → [`00b3af6c`](#insn-00b3af6c)
- ブロック [`00b3af6c`](#insn-00b3af6c) 範囲 `[['00b3af6c', '00b3af73']]`
  - `UNCONDITIONAL_JUMP` [`00b3af70`](#insn-00b3af70) → [`00b3af7c`](#insn-00b3af7c)
- ブロック [`00b3af74`](#insn-00b3af74) 範囲 `[['00b3af74', '00b3af7b']]`
  - `FALL_THROUGH` [`00b3af78`](#insn-00b3af78) → [`00b3af7c`](#insn-00b3af7c)
- ブロック [`00b3af7c`](#insn-00b3af7c) 範囲 `[['00b3af7c', '00b3af83']]`
  - `FALL_THROUGH` [`00b3af80`](#insn-00b3af80) → [`00b3af84`](#insn-00b3af84)
- ブロック [`00b3af84`](#insn-00b3af84) 範囲 `[['00b3af84', '00b3af87']]`
  - `FALL_THROUGH` [`00b3af84`](#insn-00b3af84) → [`00b3af88`](#insn-00b3af88)
- ブロック [`00b3af88`](#insn-00b3af88) 範囲 `[['00b3af88', '00b3af8f']]`
  - `CONDITIONAL_JUMP` [`00b3af8c`](#insn-00b3af8c) → [`00b3af98`](#insn-00b3af98)
  - `FALL_THROUGH` [`00b3af8c`](#insn-00b3af8c) → [`00b3af90`](#insn-00b3af90)
- ブロック [`00b3af90`](#insn-00b3af90) 範囲 `[['00b3af90', '00b3af97']]`
  - `FALL_THROUGH` [`00b3af94`](#insn-00b3af94) → [`00b3af98`](#insn-00b3af98)
- ブロック [`00b3af98`](#insn-00b3af98) 範囲 `[['00b3af98', '00b3afa7']]`

## 命令位置別の参照

- [`00b3aecc`](#insn-00b3aecc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3aed0`](#insn-00b3aed0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3aee0`](#insn-00b3aee0) → [`00b3af08`](#insn-00b3af08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3aee8`](#insn-00b3aee8) → [`00b3af98`](#insn-00b3af98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3aef8`](#insn-00b3aef8) → [`00b3af14`](#insn-00b3af14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3aefc`](#insn-00b3aefc) → [`00b3af28`](#insn-00b3af28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3af04`](#insn-00b3af04) → [`00b3af1c`](#insn-00b3af1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3af08`](#insn-00b3af08) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3af0c`](#insn-00b3af0c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3af38`](#insn-00b3af38) → [`00b3af48`](#insn-00b3af48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3af3c`](#insn-00b3af3c) → [`00b3af5c`](#insn-00b3af5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3af44`](#insn-00b3af44) → [`00b3af50`](#insn-00b3af50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3af64`](#insn-00b3af64) → [`00b3af74`](#insn-00b3af74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3af68`](#insn-00b3af68) → [`00b3af88`](#insn-00b3af88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3af70`](#insn-00b3af70) → [`00b3af7c`](#insn-00b3af7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3af8c`](#insn-00b3af8c) → [`00b3af98`](#insn-00b3af98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3af94`](#insn-00b3af94) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00b3af9c`](#insn-00b3af9c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3afa0`](#insn-00b3afa0) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3afa4`](#insn-00b3afa4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b3aecc`](#insn-00b3aecc)

~~~json
{
  "source": "00b3aecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3aed0`](#insn-00b3aed0)

~~~json
{
  "source": "00b3aed0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3aee0`](#insn-00b3aee0)

~~~json
{
  "source": "00b3aee0",
  "target": "00b3af08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3aee8`](#insn-00b3aee8)

~~~json
{
  "source": "00b3aee8",
  "target": "00b3af98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3aef8`](#insn-00b3aef8)

~~~json
{
  "source": "00b3aef8",
  "target": "00b3af14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3aefc`](#insn-00b3aefc)

~~~json
{
  "source": "00b3aefc",
  "target": "00b3af28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3af04`](#insn-00b3af04)

~~~json
{
  "source": "00b3af04",
  "target": "00b3af1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3af08`](#insn-00b3af08)

~~~json
{
  "source": "00b3af08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3af0c`](#insn-00b3af0c)

~~~json
{
  "source": "00b3af0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3af38`](#insn-00b3af38)

~~~json
{
  "source": "00b3af38",
  "target": "00b3af48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3af3c`](#insn-00b3af3c)

~~~json
{
  "source": "00b3af3c",
  "target": "00b3af5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3af44`](#insn-00b3af44)

~~~json
{
  "source": "00b3af44",
  "target": "00b3af50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3af64`](#insn-00b3af64)

~~~json
{
  "source": "00b3af64",
  "target": "00b3af74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3af68`](#insn-00b3af68)

~~~json
{
  "source": "00b3af68",
  "target": "00b3af88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3af70`](#insn-00b3af70)

~~~json
{
  "source": "00b3af70",
  "target": "00b3af7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3af8c`](#insn-00b3af8c)

~~~json
{
  "source": "00b3af8c",
  "target": "00b3af98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3af94`](#insn-00b3af94)

~~~json
{
  "source": "00b3af94",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3af9c`](#insn-00b3af9c)

~~~json
{
  "source": "00b3af9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3afa0`](#insn-00b3afa0)

~~~json
{
  "source": "00b3afa0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3afa4`](#insn-00b3afa4)

~~~json
{
  "source": "00b3afa4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
