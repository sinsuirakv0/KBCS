# 00bbf9ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbe9f8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbe/00bbe9f8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0009.md#compare-d99e13b9998075578587fed4a4a779c1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbf9ec",
  "name": "_ZNK8firebase9messaging8internal13MessageReader29ConsumeUnregistrationReceivedEPKN3com6google8firebase9messaging3cpp32SerializedUnregistrationReceivedE",
  "size": 96,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0ef8c9db34ef1f130ea2f14af4b37c3a29c57dce6d434ecf6a843126bdeeb318",
  "source_text_sha256": "0ef8c9db34ef1f130ea2f14af4b37c3a29c57dce6d434ecf6a843126bdeeb318",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbf9ec",
        "00bbfa4b"
      ]
    ],
    "bytes_sha256": "29f206acd61809e2cf49e116926fae78f263f9c55309cf5ac3ac7f6c3be5794a",
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

## 疑似コード / UTF-8 1192 bytes

~~~c

void _ZNK8firebase9messaging8internal13MessageReader29ConsumeUnregistrationReceivedEPKN3com6google8firebase9messaging3cpp32SerializedUnregistrationReceivedE
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
      UNRECOVERED_JUMPTABLE = *(code **)(param_1 + 0x30);
    }
    else {
      uVar3 = (ulong)((ushort *)((long)param_2 - (long)*param_2))[2];
      lVar4 = 0;
      if (uVar3 != 0) {
        puVar1 = (uint *)((long)param_2 + uVar3);
        lVar4 = (long)puVar1 + (ulong)*puVar1;
      }
      UNRECOVERED_JUMPTABLE = *(code **)(param_1 + 0x30);
    }
    if (UNRECOVERED_JUMPTABLE != (code *)0x0) {
      puVar2 = &DAT_002a64e6;
      if (lVar4 != 0) {
        puVar2 = (undefined1 *)(lVar4 + 4);
      }
                    /* WARNING: Could not recover jumptable at 0x00bbfa38. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (*UNRECOVERED_JUMPTABLE)(puVar2,*(undefined8 *)(param_1 + 0x38));
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
<a id="insn-00bbf9ec"></a> `00bbf9ec` | `e1 02 00 b4` | cbz x1,0x00bbfa48 | `CONDITIONAL_JUMP`
<a id="insn-00bbf9f0"></a> `00bbf9f0` | `28 00 80 b9` | ldrsw x8,[x1] | `FALL_THROUGH`
<a id="insn-00bbf9f4"></a> `00bbf9f4` | `28 00 08 cb` | sub x8,x1,x8 | `FALL_THROUGH`
<a id="insn-00bbf9f8"></a> `00bbf9f8` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf9fc"></a> `00bbf9fc` | `3f 15 00 71` | cmp w9,#0x5 | `FALL_THROUGH`
<a id="insn-00bbfa00"></a> `00bbfa00` | `e3 01 00 54` | b.cc 0x00bbfa3c | `CONDITIONAL_JUMP`
<a id="insn-00bbfa04"></a> `00bbfa04` | `08 09 40 79` | ldrh w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bbfa08"></a> `00bbfa08` | `88 00 00 b4` | cbz x8,0x00bbfa18 | `CONDITIONAL_JUMP`
<a id="insn-00bbfa0c"></a> `00bbfa0c` | `28 00 08 8b` | add x8,x1,x8 | `FALL_THROUGH`
<a id="insn-00bbfa10"></a> `00bbfa10` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbfa14"></a> `00bbfa14` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbfa18"></a> `00bbfa18` | `02 18 40 f9` | ldr x2,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00bbfa1c"></a> `00bbfa1c` | `62 01 00 b4` | cbz x2,0x00bbfa48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfa20"></a> `00bbfa20` | `01 1c 40 f9` | ldr x1,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00bbfa24"></a> `00bbfa24` | `2a b7 ff f0` | adrp x10,0x2a6000 | `FALL_THROUGH`
<a id="insn-00bbfa28"></a> `00bbfa28` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbfa2c"></a> `00bbfa2c` | `4a 99 13 91` | add x10,x10,#0x4e6 | `FALL_THROUGH`
<a id="insn-00bbfa30"></a> `00bbfa30` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbfa34"></a> `00bbfa34` | `40 01 89 9a` | csel x0,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bbfa38"></a> `00bbfa38` | `40 00 1f d6` | br x2 | `COMPUTED_JUMP`
<a id="insn-00bbfa3c"></a> `00bbfa3c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbfa40"></a> `00bbfa40` | `02 18 40 f9` | ldr x2,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00bbfa44"></a> `00bbfa44` | `e2 fe ff b5` | cbnz x2,0x00bbfa20 | `CONDITIONAL_JUMP`
<a id="insn-00bbfa48"></a> `00bbfa48` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbf9ec`](#insn-00bbf9ec) 範囲 `[['00bbf9ec', '00bbf9ef']]`
  - `CONDITIONAL_JUMP` [`00bbf9ec`](#insn-00bbf9ec) → [`00bbfa48`](#insn-00bbfa48)
  - `FALL_THROUGH` [`00bbf9ec`](#insn-00bbf9ec) → [`00bbf9f0`](#insn-00bbf9f0)
- ブロック [`00bbf9f0`](#insn-00bbf9f0) 範囲 `[['00bbf9f0', '00bbfa03']]`
  - `CONDITIONAL_JUMP` [`00bbfa00`](#insn-00bbfa00) → [`00bbfa3c`](#insn-00bbfa3c)
  - `FALL_THROUGH` [`00bbfa00`](#insn-00bbfa00) → [`00bbfa04`](#insn-00bbfa04)
- ブロック [`00bbfa04`](#insn-00bbfa04) 範囲 `[['00bbfa04', '00bbfa0b']]`
  - `CONDITIONAL_JUMP` [`00bbfa08`](#insn-00bbfa08) → [`00bbfa18`](#insn-00bbfa18)
  - `FALL_THROUGH` [`00bbfa08`](#insn-00bbfa08) → [`00bbfa0c`](#insn-00bbfa0c)
- ブロック [`00bbfa0c`](#insn-00bbfa0c) 範囲 `[['00bbfa0c', '00bbfa17']]`
  - `FALL_THROUGH` [`00bbfa14`](#insn-00bbfa14) → [`00bbfa18`](#insn-00bbfa18)
- ブロック [`00bbfa18`](#insn-00bbfa18) 範囲 `[['00bbfa18', '00bbfa1f']]`
  - `CONDITIONAL_JUMP` [`00bbfa1c`](#insn-00bbfa1c) → [`00bbfa48`](#insn-00bbfa48)
  - `FALL_THROUGH` [`00bbfa1c`](#insn-00bbfa1c) → [`00bbfa20`](#insn-00bbfa20)
- ブロック [`00bbfa20`](#insn-00bbfa20) 範囲 `[['00bbfa20', '00bbfa3b']]`
- ブロック [`00bbfa3c`](#insn-00bbfa3c) 範囲 `[['00bbfa3c', '00bbfa47']]`
  - `CONDITIONAL_JUMP` [`00bbfa44`](#insn-00bbfa44) → [`00bbfa20`](#insn-00bbfa20)
  - `FALL_THROUGH` [`00bbfa44`](#insn-00bbfa44) → [`00bbfa48`](#insn-00bbfa48)
- ブロック [`00bbfa48`](#insn-00bbfa48) 範囲 `[['00bbfa48', '00bbfa4b']]`

## 命令位置別の参照

- [`00bbf9ec`](#insn-00bbf9ec) → [`00bbfa48`](#insn-00bbfa48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa00`](#insn-00bbfa00) → [`00bbfa3c`](#insn-00bbfa3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa08`](#insn-00bbfa08) → [`00bbfa18`](#insn-00bbfa18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa1c`](#insn-00bbfa1c) → [`00bbfa48`](#insn-00bbfa48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa44`](#insn-00bbfa44) → [`00bbfa20`](#insn-00bbfa20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbf9ec`](#insn-00bbf9ec)

~~~json
{
  "source": "00bbf9ec",
  "target": "00bbfa48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa00`](#insn-00bbfa00)

~~~json
{
  "source": "00bbfa00",
  "target": "00bbfa3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa08`](#insn-00bbfa08)

~~~json
{
  "source": "00bbfa08",
  "target": "00bbfa18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa1c`](#insn-00bbfa1c)

~~~json
{
  "source": "00bbfa1c",
  "target": "00bbfa48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa44`](#insn-00bbfa44)

~~~json
{
  "source": "00bbfa44",
  "target": "00bbfa20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
