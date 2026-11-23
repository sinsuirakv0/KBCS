# 00afdcfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afdc34`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afdc34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-5136277be5782cd277eb912e768bb71b)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afdd40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afdd40.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-644f3793db22b6ce1c95ee2c317c7655)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afdcfc",
  "name": "_ZN8firebase4Path11GetRelativeERKS0_S2_PS0_",
  "size": 184,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d31e7d4f8658c83b2257e9a89b993289a09d79d3c4d76321beeaba11d1ce427b",
  "source_text_sha256": "d31e7d4f8658c83b2257e9a89b993289a09d79d3c4d76321beeaba11d1ce427b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afdcfc",
        "00afddb3"
      ]
    ],
    "bytes_sha256": "c18db24be2fd12d6600ce984ef8bf4d7bfa43408c327a42db2d20a2302020c22",
    "instruction_count": 46,
    "instruction_bytes": 184,
    "body_bytes": 184,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bde1e0](../00bde/00bde1e0.md)
- [00bdecd0](../00bde/00bdecd0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1415 bytes

~~~c

void _ZN8firebase4Path11GetRelativeERKS0_S2_PS0_
               (undefined8 param_1,undefined8 param_2,byte *param_3)

{
  ulong uVar1;
  long lVar2;
  void *pvVar3;
  undefined8 uVar4;
  byte local_58 [8];
  ulong local_50;
  void *local_48;
  char local_40;
  long local_38;
  
                    /* try { // try from 00afdcfc to 00bfdd07 has its CatchHandler @ 00afebe4 */
                    /* try { // try from 00afdd08 to 00bfdd1f has its CatchHandler @ 00afeb88 */
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00afdd20 to 00c00b67 has its CatchHandler @ 00af560c */
  _ZN8firebase4Path11GetRelativeERKS0_S2_(local_58);
  if (local_40 == '\0') {
    uVar4 = 0;
    goto LAB_00afdd8c;
  }
  if (local_58 == param_3) {
LAB_00afdd6c:
    if ((local_58[0] & 1) != 0) {
      _ZdlPv(local_48);
    }
    local_40 = '\0';
  }
  else {
    uVar1 = (ulong)(local_58[0] >> 1);
    pvVar3 = (void *)((ulong)local_58 | 1);
    if ((local_58[0] & 1) != 0) {
      uVar1 = local_50;
      pvVar3 = local_48;
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (param_3,pvVar3,uVar1);
    if (local_40 != '\0') goto LAB_00afdd6c;
  }
  uVar4 = 1;
LAB_00afdd8c:
  if (*(long *)(lVar2 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(uVar4);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afdcfc"></a> `00afdcfc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00afdd00"></a> `00afdd00` | `f5 1b 00 f9` | str x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afdd04"></a> `00afdd04` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afdd08"></a> `00afdd08` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afdd0c"></a> `00afdd0c` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00afdd10"></a> `00afdd10` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00afdd14"></a> `00afdd14` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00afdd18"></a> `00afdd18` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00afdd1c"></a> `00afdd1c` | `f5 23 00 91` | add x21,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afdd20"></a> `00afdd20` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00afdd24"></a> `00afdd24` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afdd28"></a> `00afdd28` | `ea 83 03 94` | bl 0x00bdecd0 | `UNCONDITIONAL_CALL`
<a id="insn-00afdd2c"></a> `00afdd2c` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afdd30"></a> `00afdd30` | `c8 02 00 34` | cbz w8,0x00afdd88 | `CONDITIONAL_JUMP`
<a id="insn-00afdd34"></a> `00afdd34` | `bf 02 13 eb` | cmp x21,x19 | `FALL_THROUGH`
<a id="insn-00afdd38"></a> `00afdd38` | `a0 01 00 54` | b.eq 0x00afdd6c | `CONDITIONAL_JUMP`
<a id="insn-00afdd3c"></a> `00afdd3c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afdd40"></a> `00afdd40` | `ea 27 41 a9` | ldp x10,x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afdd44"></a> `00afdd44` | `eb 23 00 91` | add x11,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afdd48"></a> `00afdd48` | `6b 01 40 b2` | orr x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00afdd4c"></a> `00afdd4c` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afdd50"></a> `00afdd50` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afdd54"></a> `00afdd54` | `61 01 89 9a` | csel x1,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00afdd58"></a> `00afdd58` | `82 01 8a 9a` | csel x2,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00afdd5c"></a> `00afdd5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afdd60"></a> `00afdd60` | `20 81 03 94` | bl 0x00bde1e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afdd64"></a> `00afdd64` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afdd68"></a> `00afdd68` | `c8 00 00 34` | cbz w8,0x00afdd80 | `CONDITIONAL_JUMP`
<a id="insn-00afdd6c"></a> `00afdd6c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afdd70"></a> `00afdd70` | `68 00 00 36` | tbz w8,#0x0,0x00afdd7c | `CONDITIONAL_JUMP`
<a id="insn-00afdd74"></a> `00afdd74` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00afdd78"></a> `00afdd78` | `a6 74 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00afdd7c"></a> `00afdd7c` | `ff 83 00 39` | strb wzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afdd80"></a> `00afdd80` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00afdd84"></a> `00afdd84` | `02 00 00 14` | b 0x00afdd8c | `UNCONDITIONAL_JUMP`
<a id="insn-00afdd88"></a> `00afdd88` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00afdd8c"></a> `00afdd8c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00afdd90"></a> `00afdd90` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00afdd94"></a> `00afdd94` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afdd98"></a> `00afdd98` | `c1 00 00 54` | b.ne 0x00afddb0 | `CONDITIONAL_JUMP`
<a id="insn-00afdd9c"></a> `00afdd9c` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afdda0"></a> `00afdda0` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afdda4"></a> `00afdda4` | `f5 1b 40 f9` | ldr x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afdda8"></a> `00afdda8` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00afddac"></a> `00afddac` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afddb0"></a> `00afddb0` | `a4 74 03 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afdcfc`](#insn-00afdcfc) 範囲 `[['00afdcfc', '00afdd07']]`
  - `FALL_THROUGH` [`00afdd04`](#insn-00afdd04) → [`00afdd08`](#insn-00afdd08)
- ブロック [`00afdd08`](#insn-00afdd08) 範囲 `[['00afdd08', '00afdd1f']]`
  - `FALL_THROUGH` [`00afdd1c`](#insn-00afdd1c) → [`00afdd20`](#insn-00afdd20)
- ブロック [`00afdd20`](#insn-00afdd20) 範囲 `[['00afdd20', '00afdd33']]`
  - `CONDITIONAL_JUMP` [`00afdd30`](#insn-00afdd30) → [`00afdd88`](#insn-00afdd88)
  - `FALL_THROUGH` [`00afdd30`](#insn-00afdd30) → [`00afdd34`](#insn-00afdd34)
- ブロック [`00afdd34`](#insn-00afdd34) 範囲 `[['00afdd34', '00afdd3b']]`
  - `CONDITIONAL_JUMP` [`00afdd38`](#insn-00afdd38) → [`00afdd6c`](#insn-00afdd6c)
  - `FALL_THROUGH` [`00afdd38`](#insn-00afdd38) → [`00afdd3c`](#insn-00afdd3c)
- ブロック [`00afdd3c`](#insn-00afdd3c) 範囲 `[['00afdd3c', '00afdd6b']]`
  - `CONDITIONAL_JUMP` [`00afdd68`](#insn-00afdd68) → [`00afdd80`](#insn-00afdd80)
  - `FALL_THROUGH` [`00afdd68`](#insn-00afdd68) → [`00afdd6c`](#insn-00afdd6c)
- ブロック [`00afdd6c`](#insn-00afdd6c) 範囲 `[['00afdd6c', '00afdd73']]`
  - `CONDITIONAL_JUMP` [`00afdd70`](#insn-00afdd70) → [`00afdd7c`](#insn-00afdd7c)
  - `FALL_THROUGH` [`00afdd70`](#insn-00afdd70) → [`00afdd74`](#insn-00afdd74)
- ブロック [`00afdd74`](#insn-00afdd74) 範囲 `[['00afdd74', '00afdd7b']]`
  - `FALL_THROUGH` [`00afdd78`](#insn-00afdd78) → [`00afdd7c`](#insn-00afdd7c)
- ブロック [`00afdd7c`](#insn-00afdd7c) 範囲 `[['00afdd7c', '00afdd7f']]`
  - `FALL_THROUGH` [`00afdd7c`](#insn-00afdd7c) → [`00afdd80`](#insn-00afdd80)
- ブロック [`00afdd80`](#insn-00afdd80) 範囲 `[['00afdd80', '00afdd87']]`
  - `UNCONDITIONAL_JUMP` [`00afdd84`](#insn-00afdd84) → [`00afdd8c`](#insn-00afdd8c)
- ブロック [`00afdd88`](#insn-00afdd88) 範囲 `[['00afdd88', '00afdd8b']]`
  - `FALL_THROUGH` [`00afdd88`](#insn-00afdd88) → [`00afdd8c`](#insn-00afdd8c)
- ブロック [`00afdd8c`](#insn-00afdd8c) 範囲 `[['00afdd8c', '00afdd9b']]`
  - `CONDITIONAL_JUMP` [`00afdd98`](#insn-00afdd98) → [`00afddb0`](#insn-00afddb0)
  - `FALL_THROUGH` [`00afdd98`](#insn-00afdd98) → [`00afdd9c`](#insn-00afdd9c)
- ブロック [`00afdd9c`](#insn-00afdd9c) 範囲 `[['00afdd9c', '00afddaf']]`
- ブロック [`00afddb0`](#insn-00afddb0) 範囲 `[['00afddb0', '00afddb3']]`

## 命令位置別の参照

- [`00afdd00`](#insn-00afdd00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd04`](#insn-00afdd04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd08`](#insn-00afdd08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd20`](#insn-00afdd20) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd28`](#insn-00afdd28) → [`00bdecd0`](../00bde/00bdecd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdecd0` · 推定シンボル `None` · 推定型 `None`
- [`00afdd2c`](#insn-00afdd2c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd30`](#insn-00afdd30) → [`00afdd88`](#insn-00afdd88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd38`](#insn-00afdd38) → [`00afdd6c`](#insn-00afdd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd3c`](#insn-00afdd3c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd40`](#insn-00afdd40) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd60`](#insn-00afdd60) → [`00bde1e0`](../00bde/00bde1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1e0` · 推定シンボル `None` · 推定型 `None`
- [`00afdd64`](#insn-00afdd64) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd68`](#insn-00afdd68) → [`00afdd80`](#insn-00afdd80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd6c`](#insn-00afdd6c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd70`](#insn-00afdd70) → [`00afdd7c`](#insn-00afdd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd74`](#insn-00afdd74) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd78`](#insn-00afdd78) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00afdd7c`](#insn-00afdd7c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd84`](#insn-00afdd84) → [`00afdd8c`](#insn-00afdd8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd90`](#insn-00afdd90) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd98`](#insn-00afdd98) → [`00afddb0`](#insn-00afddb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd9c`](#insn-00afdd9c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdda0`](#insn-00afdda0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdda4`](#insn-00afdda4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afddb0`](#insn-00afddb0) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afdd00`](#insn-00afdd00)

~~~json
{
  "source": "00afdd00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd04`](#insn-00afdd04)

~~~json
{
  "source": "00afdd04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd08`](#insn-00afdd08)

~~~json
{
  "source": "00afdd08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd20`](#insn-00afdd20)

~~~json
{
  "source": "00afdd20",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd28`](#insn-00afdd28)

~~~json
{
  "source": "00afdd28",
  "target": "00bdecd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdd2c`](#insn-00afdd2c)

~~~json
{
  "source": "00afdd2c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd30`](#insn-00afdd30)

~~~json
{
  "source": "00afdd30",
  "target": "00afdd88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd38`](#insn-00afdd38)

~~~json
{
  "source": "00afdd38",
  "target": "00afdd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd3c`](#insn-00afdd3c)

~~~json
{
  "source": "00afdd3c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd40`](#insn-00afdd40)

~~~json
{
  "source": "00afdd40",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd60`](#insn-00afdd60)

~~~json
{
  "source": "00afdd60",
  "target": "00bde1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdd64`](#insn-00afdd64)

~~~json
{
  "source": "00afdd64",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd68`](#insn-00afdd68)

~~~json
{
  "source": "00afdd68",
  "target": "00afdd80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd6c`](#insn-00afdd6c)

~~~json
{
  "source": "00afdd6c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd70`](#insn-00afdd70)

~~~json
{
  "source": "00afdd70",
  "target": "00afdd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd74`](#insn-00afdd74)

~~~json
{
  "source": "00afdd74",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd78`](#insn-00afdd78)

~~~json
{
  "source": "00afdd78",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdd7c`](#insn-00afdd7c)

~~~json
{
  "source": "00afdd7c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd84`](#insn-00afdd84)

~~~json
{
  "source": "00afdd84",
  "target": "00afdd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd90`](#insn-00afdd90)

~~~json
{
  "source": "00afdd90",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd98`](#insn-00afdd98)

~~~json
{
  "source": "00afdd98",
  "target": "00afddb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd9c`](#insn-00afdd9c)

~~~json
{
  "source": "00afdd9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdda0`](#insn-00afdda0)

~~~json
{
  "source": "00afdda0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdda4`](#insn-00afdda4)

~~~json
{
  "source": "00afdda4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afddb0`](#insn-00afddb0)

~~~json
{
  "source": "00afddb0",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
