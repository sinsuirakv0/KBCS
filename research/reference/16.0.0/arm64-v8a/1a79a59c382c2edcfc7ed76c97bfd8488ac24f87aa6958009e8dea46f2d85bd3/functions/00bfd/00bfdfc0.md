# 00bfdfc0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b81578`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81578.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-7dcb2d71e0cb5b5272999435266360c9)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfe3e8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe3e8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-d74b43d3902adb1f3eb4c4b1605a9f0b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfdfc0",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7putbackEc",
  "size": 228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b4f646a7221fc9a64369924e393fc876dc06b1d0f11148d250f65262b370dedb",
  "source_text_sha256": "b4f646a7221fc9a64369924e393fc876dc06b1d0f11148d250f65262b370dedb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfdfc0",
        "00bfe0a3"
      ]
    ],
    "bytes_sha256": "173a8bdc0a93e33eb9dbb404c4d567c12dc489a31271446f022b028f94d2934a",
    "instruction_count": 57,
    "instruction_bytes": 228,
    "body_bytes": 228,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ea0](../00c57/00c57ea0.md)
- [00c599d0](../00c59/00c599d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1120 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7putbackEc(long *param_1,char param_2)

{
  int iVar1;
  long *plVar2;
  char *pcVar3;
  long lVar4;
  uint uVar5;
  char local_14 [4];
  
  lVar4 = *(long *)(*param_1 + -0x18);
  param_1[1] = 0;
  uVar5 = *(uint *)((long)param_1 + lVar4 + 0x20) & 0xfffffffd;
  _ZNSt6__ndk18ios_base5clearEj((long)param_1 + *(long *)(*param_1 + -0x18),uVar5);
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_14,param_1,1);
  if (local_14[0] == '\0') {
    uVar5 = uVar5 | 4;
    goto LAB_00bfe074;
  }
  plVar2 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
  if (plVar2 != (long *)0x0) {
    if ((plVar2[2] != plVar2[3]) && (pcVar3 = (char *)(plVar2[3] + -1), *pcVar3 == param_2)) {
      plVar2[3] = (long)pcVar3;
      goto LAB_00bfe074;
    }
    iVar1 = (**(code **)(*plVar2 + 0x58))(plVar2,param_2);
    if (iVar1 != -1) goto LAB_00bfe074;
  }
  uVar5 = uVar5 | 1;
LAB_00bfe074:
  lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar4,*(uint *)(lVar4 + 0x20) | uVar5);
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfdfc0"></a> `00bfdfc0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfdfc4"></a> `00bfdfc4` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bfdfc8"></a> `00bfdfc8` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfdfcc"></a> `00bfdfcc` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfdfd0"></a> `00bfdfd0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfdfd4"></a> `00bfdfd4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfdfd8"></a> `00bfdfd8` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-00bfdfdc"></a> `00bfdfdc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfdfe0"></a> `00bfdfe0` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfdfe4"></a> `00bfdfe4` | `1f 04 00 f9` | str xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdfe8"></a> `00bfdfe8` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfdfec"></a> `00bfdfec` | `09 00 09 8b` | add x9,x0,x9 | `FALL_THROUGH`
<a id="insn-00bfdff0"></a> `00bfdff0` | `29 21 40 b9` | ldr w9,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bfdff4"></a> `00bfdff4` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00bfdff8"></a> `00bfdff8` | `34 79 1e 12` | and w20,w9,#0xfffffffd | `FALL_THROUGH`
<a id="insn-00bfdffc"></a> `00bfdffc` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00bfe000"></a> `00bfe000` | `a8 67 01 94` | bl 0x00c57ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfe004"></a> `00bfe004` | `a0 73 00 91` | add x0,x29,#0x1c | `FALL_THROUGH`
<a id="insn-00bfe008"></a> `00bfe008` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfe00c"></a> `00bfe00c` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bfe010"></a> `00bfe010` | `70 6e 01 94` | bl 0x00c599d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfe014"></a> `00bfe014` | `a8 73 40 39` | ldrb w8,[x29, #0x1c] | `FALL_THROUGH`
<a id="insn-00bfe018"></a> `00bfe018` | `c8 01 00 34` | cbz w8,0x00bfe050 | `CONDITIONAL_JUMP`
<a id="insn-00bfe01c"></a> `00bfe01c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfe020"></a> `00bfe020` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfe024"></a> `00bfe024` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfe028"></a> `00bfe028` | `00 15 40 f9` | ldr x0,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bfe02c"></a> `00bfe02c` | `20 02 00 b4` | cbz x0,0x00bfe070 | `CONDITIONAL_JUMP`
<a id="insn-00bfe030"></a> `00bfe030` | `09 20 41 a9` | ldp x9,x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bfe034"></a> `00bfe034` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bfe038"></a> `00bfe038` | `00 01 00 54` | b.eq 0x00bfe058 | `CONDITIONAL_JUMP`
<a id="insn-00bfe03c"></a> `00bfe03c` | `09 fd 5f 38` | ldrb w9,[x8, #-0x1]! | `FALL_THROUGH`
<a id="insn-00bfe040"></a> `00bfe040` | `3f 01 35 6b` | cmp w9,w21, UXTB  | `FALL_THROUGH`
<a id="insn-00bfe044"></a> `00bfe044` | `a1 00 00 54` | b.ne 0x00bfe058 | `CONDITIONAL_JUMP`
<a id="insn-00bfe048"></a> `00bfe048` | `08 0c 00 f9` | str x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfe04c"></a> `00bfe04c` | `0a 00 00 14` | b 0x00bfe074 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfe050"></a> `00bfe050` | `94 02 1e 32` | orr w20,w20,#0x4 | `FALL_THROUGH`
<a id="insn-00bfe054"></a> `00bfe054` | `08 00 00 14` | b 0x00bfe074 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfe058"></a> `00bfe058` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfe05c"></a> `00bfe05c` | `08 2d 40 f9` | ldr x8,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-00bfe060"></a> `00bfe060` | `a1 1e 00 12` | and w1,w21,#0xff | `FALL_THROUGH`
<a id="insn-00bfe064"></a> `00bfe064` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfe068"></a> `00bfe068` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfe06c"></a> `00bfe06c` | `41 00 00 54` | b.ne 0x00bfe074 | `CONDITIONAL_JUMP`
<a id="insn-00bfe070"></a> `00bfe070` | `94 02 00 32` | orr w20,w20,#0x1 | `FALL_THROUGH`
<a id="insn-00bfe074"></a> `00bfe074` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfe078"></a> `00bfe078` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfe07c"></a> `00bfe07c` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfe080"></a> `00bfe080` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfe084"></a> `00bfe084` | `01 01 14 2a` | orr w1,w8,w20 | `FALL_THROUGH`
<a id="insn-00bfe088"></a> `00bfe088` | `86 67 01 94` | bl 0x00c57ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfe08c"></a> `00bfe08c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfe090"></a> `00bfe090` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfe094"></a> `00bfe094` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfe098"></a> `00bfe098` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bfe09c"></a> `00bfe09c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfe0a0"></a> `00bfe0a0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfdfc0`](#insn-00bfdfc0) 範囲 `[['00bfdfc0', '00bfe01b']]`
  - `CONDITIONAL_JUMP` [`00bfe018`](#insn-00bfe018) → [`00bfe050`](#insn-00bfe050)
  - `FALL_THROUGH` [`00bfe018`](#insn-00bfe018) → [`00bfe01c`](#insn-00bfe01c)
- ブロック [`00bfe01c`](#insn-00bfe01c) 範囲 `[['00bfe01c', '00bfe02f']]`
  - `CONDITIONAL_JUMP` [`00bfe02c`](#insn-00bfe02c) → [`00bfe070`](#insn-00bfe070)
  - `FALL_THROUGH` [`00bfe02c`](#insn-00bfe02c) → [`00bfe030`](#insn-00bfe030)
- ブロック [`00bfe030`](#insn-00bfe030) 範囲 `[['00bfe030', '00bfe03b']]`
  - `CONDITIONAL_JUMP` [`00bfe038`](#insn-00bfe038) → [`00bfe058`](#insn-00bfe058)
  - `FALL_THROUGH` [`00bfe038`](#insn-00bfe038) → [`00bfe03c`](#insn-00bfe03c)
- ブロック [`00bfe03c`](#insn-00bfe03c) 範囲 `[['00bfe03c', '00bfe047']]`
  - `CONDITIONAL_JUMP` [`00bfe044`](#insn-00bfe044) → [`00bfe058`](#insn-00bfe058)
  - `FALL_THROUGH` [`00bfe044`](#insn-00bfe044) → [`00bfe048`](#insn-00bfe048)
- ブロック [`00bfe048`](#insn-00bfe048) 範囲 `[['00bfe048', '00bfe04f']]`
  - `UNCONDITIONAL_JUMP` [`00bfe04c`](#insn-00bfe04c) → [`00bfe074`](#insn-00bfe074)
- ブロック [`00bfe050`](#insn-00bfe050) 範囲 `[['00bfe050', '00bfe057']]`
  - `UNCONDITIONAL_JUMP` [`00bfe054`](#insn-00bfe054) → [`00bfe074`](#insn-00bfe074)
- ブロック [`00bfe058`](#insn-00bfe058) 範囲 `[['00bfe058', '00bfe06f']]`
  - `CONDITIONAL_JUMP` [`00bfe06c`](#insn-00bfe06c) → [`00bfe074`](#insn-00bfe074)
  - `FALL_THROUGH` [`00bfe06c`](#insn-00bfe06c) → [`00bfe070`](#insn-00bfe070)
- ブロック [`00bfe070`](#insn-00bfe070) 範囲 `[['00bfe070', '00bfe073']]`
  - `FALL_THROUGH` [`00bfe070`](#insn-00bfe070) → [`00bfe074`](#insn-00bfe074)
- ブロック [`00bfe074`](#insn-00bfe074) 範囲 `[['00bfe074', '00bfe0a3']]`

## 命令位置別の参照

- [`00bfdfc4`](#insn-00bfdfc4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdfc8`](#insn-00bfdfc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdfcc`](#insn-00bfdfcc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe000`](#insn-00bfe000) → [`00c57ea0`](../00c57/00c57ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bfe010`](#insn-00bfe010) → [`00c599d0`](../00c59/00c599d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c599d0` · 推定シンボル `None` · 推定型 `None`
- [`00bfe014`](#insn-00bfe014) → `Stack[-0x14]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe018`](#insn-00bfe018) → [`00bfe050`](#insn-00bfe050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe02c`](#insn-00bfe02c) → [`00bfe070`](#insn-00bfe070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe038`](#insn-00bfe038) → [`00bfe058`](#insn-00bfe058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe044`](#insn-00bfe044) → [`00bfe058`](#insn-00bfe058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe04c`](#insn-00bfe04c) → [`00bfe074`](#insn-00bfe074) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe054`](#insn-00bfe054) → [`00bfe074`](#insn-00bfe074) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe06c`](#insn-00bfe06c) → [`00bfe074`](#insn-00bfe074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe088`](#insn-00bfe088) → [`00c57ea0`](../00c57/00c57ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bfe090`](#insn-00bfe090) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe094`](#insn-00bfe094) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe098`](#insn-00bfe098) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfdfc4`](#insn-00bfdfc4)

~~~json
{
  "source": "00bfdfc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdfc8`](#insn-00bfdfc8)

~~~json
{
  "source": "00bfdfc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdfcc`](#insn-00bfdfcc)

~~~json
{
  "source": "00bfdfcc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe000`](#insn-00bfe000)

~~~json
{
  "source": "00bfe000",
  "target": "00c57ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfe010`](#insn-00bfe010)

~~~json
{
  "source": "00bfe010",
  "target": "00c599d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfe014`](#insn-00bfe014)

~~~json
{
  "source": "00bfe014",
  "target": "Stack[-0x14]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe018`](#insn-00bfe018)

~~~json
{
  "source": "00bfe018",
  "target": "00bfe050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe02c`](#insn-00bfe02c)

~~~json
{
  "source": "00bfe02c",
  "target": "00bfe070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe038`](#insn-00bfe038)

~~~json
{
  "source": "00bfe038",
  "target": "00bfe058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe044`](#insn-00bfe044)

~~~json
{
  "source": "00bfe044",
  "target": "00bfe058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe04c`](#insn-00bfe04c)

~~~json
{
  "source": "00bfe04c",
  "target": "00bfe074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe054`](#insn-00bfe054)

~~~json
{
  "source": "00bfe054",
  "target": "00bfe074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe06c`](#insn-00bfe06c)

~~~json
{
  "source": "00bfe06c",
  "target": "00bfe074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe088`](#insn-00bfe088)

~~~json
{
  "source": "00bfe088",
  "target": "00c57ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfe090`](#insn-00bfe090)

~~~json
{
  "source": "00bfe090",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe094`](#insn-00bfe094)

~~~json
{
  "source": "00bfe094",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe098`](#insn-00bfe098)

~~~json
{
  "source": "00bfe098",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
