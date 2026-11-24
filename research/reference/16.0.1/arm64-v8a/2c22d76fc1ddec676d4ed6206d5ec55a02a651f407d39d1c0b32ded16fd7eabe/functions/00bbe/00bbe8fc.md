# 00bbe8fc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bbe4d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbe/00bbe4d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0009.md#compare-4ae5651095a0c675289d6b8f4e8141af)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbe998`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbe/00bbe998.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0009.md#compare-80528750ce7f19a0fd6fbee0986cafc5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbe8fc",
  "name": "_ZNK8firebase9messaging8internal13MessageReader27ConsumeRegistrationReceivedEPKN3com6google8firebase9messaging3cpp30SerializedRegistrationReceivedE",
  "size": 96,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bfb3b50a7acb9bebc29ad9ef1c0a9eadff231e56bf67a69ec6d823ba40eadb5f",
  "source_text_sha256": "bfb3b50a7acb9bebc29ad9ef1c0a9eadff231e56bf67a69ec6d823ba40eadb5f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbe8fc",
        "00bbe95b"
      ]
    ],
    "bytes_sha256": "af44d207eb683a7263ecdb341dffe811186349c0d3bb277ef728eab767697e19",
    "instruction_count": 24,
    "instruction_bytes": 96,
    "body_bytes": 96,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1188 bytes

~~~c

void _ZNK8firebase9messaging8internal13MessageReader27ConsumeRegistrationReceivedEPKN3com6google8firebase9messaging3cpp30SerializedRegistrationReceivedE
               (long param_1,int *param_2)

{
  uint *puVar1;
  undefined1 *puVar2;
  code *UNRECOVERED_JUMPTABLE;
  ulong uVar3;
  long lVar4;
  
  if (param_2 != (int *)0x0) {
    if (*(ushort *)((long)param_2 - (long)*param_2) < 5) {
      lVar4 = 0;
      UNRECOVERED_JUMPTABLE = *(code **)(param_1 + 0x20);
    }
    else {
      uVar3 = (ulong)((ushort *)((long)param_2 - (long)*param_2))[2];
      lVar4 = 0;
      if (uVar3 != 0) {
        puVar1 = (uint *)((long)param_2 + uVar3);
        lVar4 = (long)puVar1 + (ulong)*puVar1;
      }
      UNRECOVERED_JUMPTABLE = *(code **)(param_1 + 0x20);
    }
    if (UNRECOVERED_JUMPTABLE != (code *)0x0) {
      puVar2 = &DAT_002a63ea;
      if (lVar4 != 0) {
        puVar2 = (undefined1 *)(lVar4 + 4);
      }
                    /* WARNING: Could not recover jumptable at 0x00bbe948. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (*UNRECOVERED_JUMPTABLE)(puVar2,*(undefined8 *)(param_1 + 0x28));
      return;
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbe8fc"></a> `00bbe8fc` | `e1 02 00 b4` | cbz x1,0x00bbe958 | `CONDITIONAL_JUMP`
<a id="insn-00bbe900"></a> `00bbe900` | `28 00 80 b9` | ldrsw x8,[x1] | `FALL_THROUGH`
<a id="insn-00bbe904"></a> `00bbe904` | `28 00 08 cb` | sub x8,x1,x8 | `FALL_THROUGH`
<a id="insn-00bbe908"></a> `00bbe908` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe90c"></a> `00bbe90c` | `3f 15 00 71` | cmp w9,#0x5 | `FALL_THROUGH`
<a id="insn-00bbe910"></a> `00bbe910` | `e3 01 00 54` | b.cc 0x00bbe94c | `CONDITIONAL_JUMP`
<a id="insn-00bbe914"></a> `00bbe914` | `08 09 40 79` | ldrh w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bbe918"></a> `00bbe918` | `88 00 00 b4` | cbz x8,0x00bbe928 | `CONDITIONAL_JUMP`
<a id="insn-00bbe91c"></a> `00bbe91c` | `28 00 08 8b` | add x8,x1,x8 | `FALL_THROUGH`
<a id="insn-00bbe920"></a> `00bbe920` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe924"></a> `00bbe924` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe928"></a> `00bbe928` | `02 10 40 f9` | ldr x2,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bbe92c"></a> `00bbe92c` | `62 01 00 b4` | cbz x2,0x00bbe958 | `CONDITIONAL_JUMP`
<a id="insn-00bbe930"></a> `00bbe930` | `01 14 40 f9` | ldr x1,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00bbe934"></a> `00bbe934` | `4a b7 ff 90` | adrp x10,0x2a6000 | `FALL_THROUGH`
<a id="insn-00bbe938"></a> `00bbe938` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe93c"></a> `00bbe93c` | `4a a9 0f 91` | add x10,x10,#0x3ea | `FALL_THROUGH`
<a id="insn-00bbe940"></a> `00bbe940` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe944"></a> `00bbe944` | `40 01 89 9a` | csel x0,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe948"></a> `00bbe948` | `40 00 1f d6` | br x2 | `COMPUTED_JUMP`
<a id="insn-00bbe94c"></a> `00bbe94c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe950"></a> `00bbe950` | `02 10 40 f9` | ldr x2,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bbe954"></a> `00bbe954` | `e2 fe ff b5` | cbnz x2,0x00bbe930 | `CONDITIONAL_JUMP`
<a id="insn-00bbe958"></a> `00bbe958` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbe8fc`](#insn-00bbe8fc) 範囲 `[['00bbe8fc', '00bbe8ff']]`
  - `CONDITIONAL_JUMP` [`00bbe8fc`](#insn-00bbe8fc) → [`00bbe958`](#insn-00bbe958)
  - `FALL_THROUGH` [`00bbe8fc`](#insn-00bbe8fc) → [`00bbe900`](#insn-00bbe900)
- ブロック [`00bbe900`](#insn-00bbe900) 範囲 `[['00bbe900', '00bbe913']]`
  - `CONDITIONAL_JUMP` [`00bbe910`](#insn-00bbe910) → [`00bbe94c`](#insn-00bbe94c)
  - `FALL_THROUGH` [`00bbe910`](#insn-00bbe910) → [`00bbe914`](#insn-00bbe914)
- ブロック [`00bbe914`](#insn-00bbe914) 範囲 `[['00bbe914', '00bbe91b']]`
  - `CONDITIONAL_JUMP` [`00bbe918`](#insn-00bbe918) → [`00bbe928`](#insn-00bbe928)
  - `FALL_THROUGH` [`00bbe918`](#insn-00bbe918) → [`00bbe91c`](#insn-00bbe91c)
- ブロック [`00bbe91c`](#insn-00bbe91c) 範囲 `[['00bbe91c', '00bbe927']]`
  - `FALL_THROUGH` [`00bbe924`](#insn-00bbe924) → [`00bbe928`](#insn-00bbe928)
- ブロック [`00bbe928`](#insn-00bbe928) 範囲 `[['00bbe928', '00bbe92f']]`
  - `CONDITIONAL_JUMP` [`00bbe92c`](#insn-00bbe92c) → [`00bbe958`](#insn-00bbe958)
  - `FALL_THROUGH` [`00bbe92c`](#insn-00bbe92c) → [`00bbe930`](#insn-00bbe930)
- ブロック [`00bbe930`](#insn-00bbe930) 範囲 `[['00bbe930', '00bbe94b']]`
- ブロック [`00bbe94c`](#insn-00bbe94c) 範囲 `[['00bbe94c', '00bbe957']]`
  - `CONDITIONAL_JUMP` [`00bbe954`](#insn-00bbe954) → [`00bbe930`](#insn-00bbe930)
  - `FALL_THROUGH` [`00bbe954`](#insn-00bbe954) → [`00bbe958`](#insn-00bbe958)
- ブロック [`00bbe958`](#insn-00bbe958) 範囲 `[['00bbe958', '00bbe95b']]`

## 命令位置別の参照

- [`00bbe8fc`](#insn-00bbe8fc) → [`00bbe958`](#insn-00bbe958) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe910`](#insn-00bbe910) → [`00bbe94c`](#insn-00bbe94c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe918`](#insn-00bbe918) → [`00bbe928`](#insn-00bbe928) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe92c`](#insn-00bbe92c) → [`00bbe958`](#insn-00bbe958) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe954`](#insn-00bbe954) → [`00bbe930`](#insn-00bbe930) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbe8fc`](#insn-00bbe8fc)

~~~json
{
  "source": "00bbe8fc",
  "target": "00bbe958",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe910`](#insn-00bbe910)

~~~json
{
  "source": "00bbe910",
  "target": "00bbe94c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe918`](#insn-00bbe918)

~~~json
{
  "source": "00bbe918",
  "target": "00bbe928",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe92c`](#insn-00bbe92c)

~~~json
{
  "source": "00bbe92c",
  "target": "00bbe958",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe954`](#insn-00bbe954)

~~~json
{
  "source": "00bbe954",
  "target": "00bbe930",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
