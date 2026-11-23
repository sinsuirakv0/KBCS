# 00bcfa9c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcfb64`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfb64.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-2ab12b192c6d6ee9d23efa82abc12985)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfa9c",
  "name": "FUN_00bcfa9c",
  "size": 228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f7f84e9d827d6019ad3f4de1eb1cf7bb9123be6f4dd1516077eb4a96e0ca183e",
  "source_text_sha256": "f7f84e9d827d6019ad3f4de1eb1cf7bb9123be6f4dd1516077eb4a96e0ca183e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcfa9c",
        "00bcfb7f"
      ]
    ],
    "bytes_sha256": "1b91d928bd4aeba74c504cb9d48b74c144649c220630456a90faf9c776b0eed8",
    "instruction_count": 57,
    "instruction_bytes": 228,
    "body_bytes": 228,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bc81c8](../00bc8/00bc81c8.md)
- [00bdd150](../00bdd/00bdd150.md)
- [00bde1c0](../00bde/00bde1c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1780 bytes

~~~c

void FUN_00bcfa9c(long param_1,undefined8 *param_2)

{
  void *pvVar1;
  long lVar2;
  size_t sVar3;
  ulong uVar4;
  
                    /* try { // try from 00bcfaa8 to 00ccfaaf has its CatchHandler @ 00bcfc6c */
  lVar2 = param_2[1];
  pvVar1 = (void *)*param_2;
  uVar4 = lVar2 + 1;
  *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + 1;
                    /* try { // try from 00bcfad0 to 00ccfad7 has its CatchHandler @ 00bcfcec */
  if ((ulong)param_2[2] < uVar4) {
    sVar3 = param_2[2] * 2;
    uVar4 = lVar2 + 0x3e1;
    if (sVar3 < uVar4 || sVar3 - uVar4 == 0) {
      sVar3 = uVar4;
    }
    param_2[2] = sVar3;
    pvVar1 = realloc(pvVar1,sVar3);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
    uVar4 = lVar2 + 1;
  }
  param_2[1] = uVar4;
                    /* try { // try from 00bcfb04 to 00ccfb0b has its CatchHandler @ 00bcfcdc */
  *(undefined1 *)((long)pvVar1 + lVar2) = 0x5b;
                    /* try { // try from 00bcfb0c to 00ccfb6b has its CatchHandler @ 00bcfd04 */
  FUN_00bc81c8(param_1 + 0x10,param_2);
  lVar2 = param_2[1];
  pvVar1 = (void *)*param_2;
  uVar4 = lVar2 + 1;
  *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + -1;
  if ((ulong)param_2[2] < uVar4) {
    sVar3 = param_2[2] * 2;
    uVar4 = lVar2 + 0x3e1;
    if (sVar3 < uVar4 || sVar3 - uVar4 == 0) {
      sVar3 = uVar4;
    }
    param_2[2] = sVar3;
    pvVar1 = realloc(pvVar1,sVar3);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
    uVar4 = lVar2 + 1;
  }
  param_2[1] = uVar4;
  *(undefined1 *)((long)pvVar1 + lVar2) = 0x5d;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcfa9c"></a> `00bcfa9c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcfaa0"></a> `00bcfaa0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcfaa4"></a> `00bcfaa4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfaa8"></a> `00bcfaa8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcfaac"></a> `00bcfaac` | `28 a8 40 a9` | ldp x8,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfab0"></a> `00bcfab0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcfab4"></a> `00bcfab4` | `2b 20 40 b9` | ldr w11,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfab8"></a> `00bcfab8` | `20 00 40 f9` | ldr x0,[x1] | `FALL_THROUGH`
<a id="insn-00bcfabc"></a> `00bcfabc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcfac0"></a> `00bcfac0` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfac4"></a> `00bcfac4` | `6b 05 00 11` | add w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfac8"></a> `00bcfac8` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcfacc"></a> `00bcfacc` | `2b 20 00 b9` | str w11,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfad0"></a> `00bcfad0` | `69 01 00 54` | b.ls 0x00bcfafc | `CONDITIONAL_JUMP`
<a id="insn-00bcfad4"></a> `00bcfad4` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfad8"></a> `00bcfad8` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bcfadc"></a> `00bcfadc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcfae0"></a> `00bcfae0` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcfae4"></a> `00bcfae4` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfae8"></a> `00bcfae8` | `9a 35 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfaec"></a> `00bcfaec` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcfaf0"></a> `00bcfaf0` | `40 04 00 b4` | cbz x0,0x00bcfb78 | `CONDITIONAL_JUMP`
<a id="insn-00bcfaf4"></a> `00bcfaf4` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfaf8"></a> `00bcfaf8` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfafc"></a> `00bcfafc` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfb00"></a> `00bcfb00` | `69 0b 80 52` | mov w9,#0x5b | `FALL_THROUGH`
<a id="insn-00bcfb04"></a> `00bcfb04` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcfb08"></a> `00bcfb08` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bcfb0c"></a> `00bcfb0c` | `80 42 00 91` | add x0,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00bcfb10"></a> `00bcfb10` | `ae e1 ff 97` | bl 0x00bc81c8 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfb14"></a> `00bcfb14` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfb18"></a> `00bcfb18` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfb1c"></a> `00bcfb1c` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcfb20"></a> `00bcfb20` | `6b 05 00 51` | sub w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfb24"></a> `00bcfb24` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfb28"></a> `00bcfb28` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfb2c"></a> `00bcfb2c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcfb30"></a> `00bcfb30` | `69 01 00 54` | b.ls 0x00bcfb5c | `CONDITIONAL_JUMP`
<a id="insn-00bcfb34"></a> `00bcfb34` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfb38"></a> `00bcfb38` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bcfb3c"></a> `00bcfb3c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcfb40"></a> `00bcfb40` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcfb44"></a> `00bcfb44` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfb48"></a> `00bcfb48` | `82 35 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfb4c"></a> `00bcfb4c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcfb50"></a> `00bcfb50` | `60 01 00 b4` | cbz x0,0x00bcfb7c | `CONDITIONAL_JUMP`
<a id="insn-00bcfb54"></a> `00bcfb54` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfb58"></a> `00bcfb58` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfb5c"></a> `00bcfb5c` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfb60"></a> `00bcfb60` | `a9 0b 80 52` | mov w9,#0x5d | `FALL_THROUGH`
<a id="insn-00bcfb64"></a> `00bcfb64` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bcfb68"></a> `00bcfb68` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfb6c"></a> `00bcfb6c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcfb70"></a> `00bcfb70` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcfb74"></a> `00bcfb74` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcfb78"></a> `00bcfb78` | `92 39 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bcfb7c"></a> `00bcfb7c` | `91 39 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcfa9c`](#insn-00bcfa9c) 範囲 `[['00bcfa9c', '00bcfaa7']]`
  - `FALL_THROUGH` [`00bcfaa4`](#insn-00bcfaa4) → [`00bcfaa8`](#insn-00bcfaa8)
- ブロック [`00bcfaa8`](#insn-00bcfaa8) 範囲 `[['00bcfaa8', '00bcfacf']]`
  - `FALL_THROUGH` [`00bcfacc`](#insn-00bcfacc) → [`00bcfad0`](#insn-00bcfad0)
- ブロック [`00bcfad0`](#insn-00bcfad0) 範囲 `[['00bcfad0', '00bcfad3']]`
  - `CONDITIONAL_JUMP` [`00bcfad0`](#insn-00bcfad0) → [`00bcfafc`](#insn-00bcfafc)
  - `FALL_THROUGH` [`00bcfad0`](#insn-00bcfad0) → [`00bcfad4`](#insn-00bcfad4)
- ブロック [`00bcfad4`](#insn-00bcfad4) 範囲 `[['00bcfad4', '00bcfaf3']]`
  - `CONDITIONAL_JUMP` [`00bcfaf0`](#insn-00bcfaf0) → [`00bcfb78`](#insn-00bcfb78)
  - `FALL_THROUGH` [`00bcfaf0`](#insn-00bcfaf0) → [`00bcfaf4`](#insn-00bcfaf4)
- ブロック [`00bcfaf4`](#insn-00bcfaf4) 範囲 `[['00bcfaf4', '00bcfafb']]`
  - `FALL_THROUGH` [`00bcfaf8`](#insn-00bcfaf8) → [`00bcfafc`](#insn-00bcfafc)
- ブロック [`00bcfafc`](#insn-00bcfafc) 範囲 `[['00bcfafc', '00bcfb03']]`
  - `FALL_THROUGH` [`00bcfb00`](#insn-00bcfb00) → [`00bcfb04`](#insn-00bcfb04)
- ブロック [`00bcfb04`](#insn-00bcfb04) 範囲 `[['00bcfb04', '00bcfb0b']]`
  - `FALL_THROUGH` [`00bcfb08`](#insn-00bcfb08) → [`00bcfb0c`](#insn-00bcfb0c)
- ブロック [`00bcfb0c`](#insn-00bcfb0c) 範囲 `[['00bcfb0c', '00bcfb33']]`
  - `CONDITIONAL_JUMP` [`00bcfb30`](#insn-00bcfb30) → [`00bcfb5c`](#insn-00bcfb5c)
  - `FALL_THROUGH` [`00bcfb30`](#insn-00bcfb30) → [`00bcfb34`](#insn-00bcfb34)
- ブロック [`00bcfb34`](#insn-00bcfb34) 範囲 `[['00bcfb34', '00bcfb53']]`
  - `CONDITIONAL_JUMP` [`00bcfb50`](#insn-00bcfb50) → [`00bcfb7c`](#insn-00bcfb7c)
  - `FALL_THROUGH` [`00bcfb50`](#insn-00bcfb50) → [`00bcfb54`](#insn-00bcfb54)
- ブロック [`00bcfb54`](#insn-00bcfb54) 範囲 `[['00bcfb54', '00bcfb5b']]`
  - `FALL_THROUGH` [`00bcfb58`](#insn-00bcfb58) → [`00bcfb5c`](#insn-00bcfb5c)
- ブロック [`00bcfb5c`](#insn-00bcfb5c) 範囲 `[['00bcfb5c', '00bcfb77']]`
- ブロック [`00bcfb78`](#insn-00bcfb78) 範囲 `[['00bcfb78', '00bcfb7b']]`
- ブロック [`00bcfb7c`](#insn-00bcfb7c) 範囲 `[['00bcfb7c', '00bcfb7f']]`

## 命令位置別の参照

- [`00bcfaa0`](#insn-00bcfaa0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfaa4`](#insn-00bcfaa4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfad0`](#insn-00bcfad0) → [`00bcfafc`](#insn-00bcfafc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfae8`](#insn-00bcfae8) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcfaf0`](#insn-00bcfaf0) → [`00bcfb78`](#insn-00bcfb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb10`](#insn-00bcfb10) → [`00bc81c8`](../00bc8/00bc81c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc81c8` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb30`](#insn-00bcfb30) → [`00bcfb5c`](#insn-00bcfb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb48`](#insn-00bcfb48) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb50`](#insn-00bcfb50) → [`00bcfb7c`](#insn-00bcfb7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb68`](#insn-00bcfb68) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb6c`](#insn-00bcfb6c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb78`](#insn-00bcfb78) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb7c`](#insn-00bcfb7c) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcfaa0`](#insn-00bcfaa0)

~~~json
{
  "source": "00bcfaa0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfaa4`](#insn-00bcfaa4)

~~~json
{
  "source": "00bcfaa4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfad0`](#insn-00bcfad0)

~~~json
{
  "source": "00bcfad0",
  "target": "00bcfafc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfae8`](#insn-00bcfae8)

~~~json
{
  "source": "00bcfae8",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfaf0`](#insn-00bcfaf0)

~~~json
{
  "source": "00bcfaf0",
  "target": "00bcfb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb10`](#insn-00bcfb10)

~~~json
{
  "source": "00bcfb10",
  "target": "00bc81c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfb30`](#insn-00bcfb30)

~~~json
{
  "source": "00bcfb30",
  "target": "00bcfb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb48`](#insn-00bcfb48)

~~~json
{
  "source": "00bcfb48",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfb50`](#insn-00bcfb50)

~~~json
{
  "source": "00bcfb50",
  "target": "00bcfb7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb68`](#insn-00bcfb68)

~~~json
{
  "source": "00bcfb68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb6c`](#insn-00bcfb6c)

~~~json
{
  "source": "00bcfb6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb78`](#insn-00bcfb78)

~~~json
{
  "source": "00bcfb78",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfb7c`](#insn-00bcfb7c)

~~~json
{
  "source": "00bcfb7c",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
