# 00bfa8fc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfa4d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa4d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-03aed0459e0820e6f6bca5c0a4c9c78c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfa998`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa998.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-e708b96c8cd2d57ad54927d4af4f1b9f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfa8fc",
  "name": "FUN_00bfa8fc",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "39a4b5f099564c1a5a53906ce3ce6ff39142f4b259d2a93e06fd36c28708cf0b",
  "source_text_sha256": "39a4b5f099564c1a5a53906ce3ce6ff39142f4b259d2a93e06fd36c28708cf0b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfa8fc",
        "00bfa9c3"
      ]
    ],
    "bytes_sha256": "bfb527682876416b2ddf81d988cef75027c15a32bc5de7eaed68e57a14bf2f55",
    "instruction_count": 50,
    "instruction_bytes": 200,
    "body_bytes": 200,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bfabf0](../00bfa/00bfabf0.md)

## 呼び出し先

- [00c53d00](../00c53/00c53d00.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c580f0](../00c58/00c580f0.md)
- [00c58380](../00c58/00c58380.md)
- [00c5e250](../00c5e/00c5e250.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 950 bytes

~~~c

void FUN_00bfa8fc(undefined8 *param_1)

{
  undefined8 *puVar1;
  long lVar2;
  void *pvVar3;
  long *plVar4;
  undefined8 *puVar5;
  
  puVar1 = (undefined8 *)param_1[4];
  for (puVar5 = (undefined8 *)param_1[3]; puVar5 != puVar1; puVar5 = puVar5 + 2) {
    _ZNSt6__ndk118condition_variable10notify_allEv(*puVar5);
    _ZNSt6__ndk15mutex6unlockEv(puVar5[1]);
  }
  puVar1 = (undefined8 *)param_1[1];
  for (puVar5 = (undefined8 *)*param_1; puVar5 != puVar1; puVar5 = puVar5 + 1) {
    _ZNSt6__ndk117__assoc_sub_state12__make_readyEv(*puVar5);
    plVar4 = (long *)*puVar5;
    lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1);
    if (lVar2 == 0) {
      (**(code **)(*plVar4 + 0x10))(plVar4);
    }
  }
  pvVar3 = (void *)param_1[3];
  if (pvVar3 != (void *)0x0) {
    param_1[4] = pvVar3;
    _ZdlPv(pvVar3);
  }
  pvVar3 = (void *)*param_1;
  if (pvVar3 == (void *)0x0) {
    return;
  }
  param_1[1] = pvVar3;
  _ZdlPv(pvVar3);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfa8fc"></a> `00bfa8fc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfa900"></a> `00bfa900` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bfa904"></a> `00bfa904` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfa908"></a> `00bfa908` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfa90c"></a> `00bfa90c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfa910"></a> `00bfa910` | `14 d4 41 a9` | ldp x20,x21,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfa914"></a> `00bfa914` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfa918"></a> `00bfa918` | `9f 02 15 eb` | cmp x20,x21 | `FALL_THROUGH`
<a id="insn-00bfa91c"></a> `00bfa91c` | `00 01 00 54` | b.eq 0x00bfa93c | `CONDITIONAL_JUMP`
<a id="insn-00bfa920"></a> `00bfa920` | `80 02 40 f9` | ldr x0,[x20] | `FALL_THROUGH`
<a id="insn-00bfa924"></a> `00bfa924` | `97 76 01 94` | bl 0x00c58380 | `UNCONDITIONAL_CALL`
<a id="insn-00bfa928"></a> `00bfa928` | `80 06 40 f9` | ldr x0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bfa92c"></a> `00bfa92c` | `f1 75 01 94` | bl 0x00c580f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfa930"></a> `00bfa930` | `94 42 00 91` | add x20,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00bfa934"></a> `00bfa934` | `9f 02 15 eb` | cmp x20,x21 | `FALL_THROUGH`
<a id="insn-00bfa938"></a> `00bfa938` | `41 ff ff 54` | b.ne 0x00bfa920 | `CONDITIONAL_JUMP`
<a id="insn-00bfa93c"></a> `00bfa93c` | `75 5a 40 a9` | ldp x21,x22,[x19] | `FALL_THROUGH`
<a id="insn-00bfa940"></a> `00bfa940` | `02 00 00 14` | b 0x00bfa948 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfa944"></a> `00bfa944` | `b5 22 00 91` | add x21,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bfa948"></a> `00bfa948` | `bf 02 16 eb` | cmp x21,x22 | `FALL_THROUGH`
<a id="insn-00bfa94c"></a> `00bfa94c` | `a0 01 00 54` | b.eq 0x00bfa980 | `CONDITIONAL_JUMP`
<a id="insn-00bfa950"></a> `00bfa950` | `a0 02 40 f9` | ldr x0,[x21] | `FALL_THROUGH`
<a id="insn-00bfa954"></a> `00bfa954` | `3f 8e 01 94` | bl 0x00c5e250 | `UNCONDITIONAL_CALL`
<a id="insn-00bfa958"></a> `00bfa958` | `b4 02 40 f9` | ldr x20,[x21] | `FALL_THROUGH`
<a id="insn-00bfa95c"></a> `00bfa95c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00bfa960"></a> `00bfa960` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00bfa964"></a> `00bfa964` | `e7 64 01 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00bfa968"></a> `00bfa968` | `e0 fe ff b5` | cbnz x0,0x00bfa944 | `CONDITIONAL_JUMP`
<a id="insn-00bfa96c"></a> `00bfa96c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bfa970"></a> `00bfa970` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfa974"></a> `00bfa974` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bfa978"></a> `00bfa978` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfa97c"></a> `00bfa97c` | `f2 ff ff 17` | b 0x00bfa944 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfa980"></a> `00bfa980` | `60 0e 40 f9` | ldr x0,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bfa984"></a> `00bfa984` | `60 00 00 b4` | cbz x0,0x00bfa990 | `CONDITIONAL_JUMP`
<a id="insn-00bfa988"></a> `00bfa988` | `60 12 00 f9` | str x0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bfa98c"></a> `00bfa98c` | `49 75 01 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfa990"></a> `00bfa990` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bfa994"></a> `00bfa994` | `e0 00 00 b4` | cbz x0,0x00bfa9b0 | `CONDITIONAL_JUMP`
<a id="insn-00bfa998"></a> `00bfa998` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfa99c"></a> `00bfa99c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfa9a0"></a> `00bfa9a0` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfa9a4"></a> `00bfa9a4` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bfa9a8"></a> `00bfa9a8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfa9ac"></a> `00bfa9ac` | `41 75 01 14` | b 0x00c57eb0 | `CALL_TERMINATOR`
<a id="insn-00bfa9b0"></a> `00bfa9b0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfa9b4"></a> `00bfa9b4` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfa9b8"></a> `00bfa9b8` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bfa9bc"></a> `00bfa9bc` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfa9c0"></a> `00bfa9c0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfa8fc`](#insn-00bfa8fc) 範囲 `[['00bfa8fc', '00bfa91f']]`
  - `CONDITIONAL_JUMP` [`00bfa91c`](#insn-00bfa91c) → [`00bfa93c`](#insn-00bfa93c)
  - `FALL_THROUGH` [`00bfa91c`](#insn-00bfa91c) → [`00bfa920`](#insn-00bfa920)
- ブロック [`00bfa920`](#insn-00bfa920) 範囲 `[['00bfa920', '00bfa93b']]`
  - `CONDITIONAL_JUMP` [`00bfa938`](#insn-00bfa938) → [`00bfa920`](#insn-00bfa920)
  - `FALL_THROUGH` [`00bfa938`](#insn-00bfa938) → [`00bfa93c`](#insn-00bfa93c)
- ブロック [`00bfa93c`](#insn-00bfa93c) 範囲 `[['00bfa93c', '00bfa943']]`
  - `UNCONDITIONAL_JUMP` [`00bfa940`](#insn-00bfa940) → [`00bfa948`](#insn-00bfa948)
- ブロック [`00bfa944`](#insn-00bfa944) 範囲 `[['00bfa944', '00bfa947']]`
  - `FALL_THROUGH` [`00bfa944`](#insn-00bfa944) → [`00bfa948`](#insn-00bfa948)
- ブロック [`00bfa948`](#insn-00bfa948) 範囲 `[['00bfa948', '00bfa94f']]`
  - `CONDITIONAL_JUMP` [`00bfa94c`](#insn-00bfa94c) → [`00bfa980`](#insn-00bfa980)
  - `FALL_THROUGH` [`00bfa94c`](#insn-00bfa94c) → [`00bfa950`](#insn-00bfa950)
- ブロック [`00bfa950`](#insn-00bfa950) 範囲 `[['00bfa950', '00bfa96b']]`
  - `CONDITIONAL_JUMP` [`00bfa968`](#insn-00bfa968) → [`00bfa944`](#insn-00bfa944)
  - `FALL_THROUGH` [`00bfa968`](#insn-00bfa968) → [`00bfa96c`](#insn-00bfa96c)
- ブロック [`00bfa96c`](#insn-00bfa96c) 範囲 `[['00bfa96c', '00bfa97f']]`
  - `UNCONDITIONAL_JUMP` [`00bfa97c`](#insn-00bfa97c) → [`00bfa944`](#insn-00bfa944)
- ブロック [`00bfa980`](#insn-00bfa980) 範囲 `[['00bfa980', '00bfa987']]`
  - `CONDITIONAL_JUMP` [`00bfa984`](#insn-00bfa984) → [`00bfa990`](#insn-00bfa990)
  - `FALL_THROUGH` [`00bfa984`](#insn-00bfa984) → [`00bfa988`](#insn-00bfa988)
- ブロック [`00bfa988`](#insn-00bfa988) 範囲 `[['00bfa988', '00bfa98f']]`
  - `FALL_THROUGH` [`00bfa98c`](#insn-00bfa98c) → [`00bfa990`](#insn-00bfa990)
- ブロック [`00bfa990`](#insn-00bfa990) 範囲 `[['00bfa990', '00bfa997']]`
  - `CONDITIONAL_JUMP` [`00bfa994`](#insn-00bfa994) → [`00bfa9b0`](#insn-00bfa9b0)
  - `FALL_THROUGH` [`00bfa994`](#insn-00bfa994) → [`00bfa998`](#insn-00bfa998)
- ブロック [`00bfa998`](#insn-00bfa998) 範囲 `[['00bfa998', '00bfa9af']]`
- ブロック [`00bfa9b0`](#insn-00bfa9b0) 範囲 `[['00bfa9b0', '00bfa9c3']]`

## 命令位置別の参照

- [`00bfa900`](#insn-00bfa900) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa904`](#insn-00bfa904) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa908`](#insn-00bfa908) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa91c`](#insn-00bfa91c) → [`00bfa93c`](#insn-00bfa93c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa924`](#insn-00bfa924) → [`00c58380`](../00c58/00c58380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58380` · 推定シンボル `None` · 推定型 `None`
- [`00bfa92c`](#insn-00bfa92c) → [`00c580f0`](../00c58/00c580f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580f0` · 推定シンボル `None` · 推定型 `None`
- [`00bfa938`](#insn-00bfa938) → [`00bfa920`](#insn-00bfa920) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa940`](#insn-00bfa940) → [`00bfa948`](#insn-00bfa948) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa94c`](#insn-00bfa94c) → [`00bfa980`](#insn-00bfa980) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa954`](#insn-00bfa954) → [`00c5e250`](../00c5e/00c5e250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e250` · 推定シンボル `None` · 推定型 `None`
- [`00bfa964`](#insn-00bfa964) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00bfa968`](#insn-00bfa968) → [`00bfa944`](#insn-00bfa944) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa97c`](#insn-00bfa97c) → [`00bfa944`](#insn-00bfa944) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa984`](#insn-00bfa984) → [`00bfa990`](#insn-00bfa990) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa98c`](#insn-00bfa98c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bfa994`](#insn-00bfa994) → [`00bfa9b0`](#insn-00bfa9b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa99c`](#insn-00bfa99c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa9a0`](#insn-00bfa9a0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa9a4`](#insn-00bfa9a4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa9ac`](#insn-00bfa9ac) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bfa9b0`](#insn-00bfa9b0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa9b4`](#insn-00bfa9b4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa9b8`](#insn-00bfa9b8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfa900`](#insn-00bfa900)

~~~json
{
  "source": "00bfa900",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa904`](#insn-00bfa904)

~~~json
{
  "source": "00bfa904",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa908`](#insn-00bfa908)

~~~json
{
  "source": "00bfa908",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa91c`](#insn-00bfa91c)

~~~json
{
  "source": "00bfa91c",
  "target": "00bfa93c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa924`](#insn-00bfa924)

~~~json
{
  "source": "00bfa924",
  "target": "00c58380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa92c`](#insn-00bfa92c)

~~~json
{
  "source": "00bfa92c",
  "target": "00c580f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa938`](#insn-00bfa938)

~~~json
{
  "source": "00bfa938",
  "target": "00bfa920",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa940`](#insn-00bfa940)

~~~json
{
  "source": "00bfa940",
  "target": "00bfa948",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa94c`](#insn-00bfa94c)

~~~json
{
  "source": "00bfa94c",
  "target": "00bfa980",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa954`](#insn-00bfa954)

~~~json
{
  "source": "00bfa954",
  "target": "00c5e250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa964`](#insn-00bfa964)

~~~json
{
  "source": "00bfa964",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa968`](#insn-00bfa968)

~~~json
{
  "source": "00bfa968",
  "target": "00bfa944",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa97c`](#insn-00bfa97c)

~~~json
{
  "source": "00bfa97c",
  "target": "00bfa944",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa984`](#insn-00bfa984)

~~~json
{
  "source": "00bfa984",
  "target": "00bfa990",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa98c`](#insn-00bfa98c)

~~~json
{
  "source": "00bfa98c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa994`](#insn-00bfa994)

~~~json
{
  "source": "00bfa994",
  "target": "00bfa9b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa99c`](#insn-00bfa99c)

~~~json
{
  "source": "00bfa99c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa9a0`](#insn-00bfa9a0)

~~~json
{
  "source": "00bfa9a0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa9a4`](#insn-00bfa9a4)

~~~json
{
  "source": "00bfa9a4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa9ac`](#insn-00bfa9ac)

~~~json
{
  "source": "00bfa9ac",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa9b0`](#insn-00bfa9b0)

~~~json
{
  "source": "00bfa9b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa9b4`](#insn-00bfa9b4)

~~~json
{
  "source": "00bfa9b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa9b8`](#insn-00bfa9b8)

~~~json
{
  "source": "00bfa9b8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
