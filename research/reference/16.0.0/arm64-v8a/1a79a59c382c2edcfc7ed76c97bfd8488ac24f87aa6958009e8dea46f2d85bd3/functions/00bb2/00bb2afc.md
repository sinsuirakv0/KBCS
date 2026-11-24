# 00bb2afc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b471d0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b471d0.md) · 移動量 `+0x6b92c`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0016.md#compare-79c40af744ed0d38cdbd7c1bc9ff7bc9)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bb2f24`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb2/00bb2f24.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/machine_only_observed-0021.md#compare-c933b37b817abe5a8c1397101f4370c9)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb2afc",
  "name": "_ZN11flatbuffers14StripExtensionERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3a1df851eaefe306625f99c503fd260bcdaf0a0f8640fe408c9de2a594b5b43",
  "source_text_sha256": "e3a1df851eaefe306625f99c503fd260bcdaf0a0f8640fe408c9de2a594b5b43",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb2afc",
        "00bb2b4f"
      ]
    ],
    "bytes_sha256": "5998d47a58312da9e4b2637c778b9f1ac99e234a45240e3507ec9cfdf5c004ad",
    "instruction_count": 21,
    "instruction_bytes": 84,
    "body_bytes": 84,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b1b0](../00c5b/00c5b1b0.md)
- [00c5b3f0](../00c5b/00c5b3f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 852 bytes

~~~c

void _ZN11flatbuffers14StripExtensionERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
               (undefined8 param_1,byte *param_2)

{
  byte *pbVar1;
  long lVar2;
  ulong uVar3;
  
  uVar3 = *(ulong *)(param_2 + 8);
  pbVar1 = *(byte **)(param_2 + 0x10);
  if ((*param_2 & 1) == 0) {
    pbVar1 = param_2 + 1;
    uVar3 = (ulong)(*param_2 >> 1);
  }
  if (uVar3 != 0) {
    do {
      if (uVar3 == 0) goto LAB_00bb2b4c;
      lVar2 = uVar3 - 1;
      uVar3 = uVar3 - 1;
    } while (pbVar1[lVar2] != 0x2e);
    if (uVar3 != 0xffffffffffffffff) {
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
                (param_1,param_2,0,uVar3,param_2);
      return;
    }
  }
LAB_00bb2b4c:
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb2afc"></a> `00bb2afc` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bb2b00"></a> `00bb2b00` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bb2b04"></a> `00bb2b04` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00bb2b08"></a> `00bb2b08` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bb2b0c"></a> `00bb2b0c` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb2b10"></a> `00bb2b10` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb2b14"></a> `00bb2b14` | `63 01 89 9a` | csel x3,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00bb2b18"></a> `00bb2b18` | `48 15 81 9a` | csinc x8,x10,x1,ne | `FALL_THROUGH`
<a id="insn-00bb2b1c"></a> `00bb2b1c` | `83 01 00 b4` | cbz x3,0x00bb2b4c | `CONDITIONAL_JUMP`
<a id="insn-00bb2b20"></a> `00bb2b20` | `63 01 00 b4` | cbz x3,0x00bb2b4c | `CONDITIONAL_JUMP`
<a id="insn-00bb2b24"></a> `00bb2b24` | `09 01 03 8b` | add x9,x8,x3 | `FALL_THROUGH`
<a id="insn-00bb2b28"></a> `00bb2b28` | `29 f1 5f 38` | ldurb w9,[x9, #-0x1] | `FALL_THROUGH`
<a id="insn-00bb2b2c"></a> `00bb2b2c` | `63 04 00 d1` | sub x3,x3,#0x1 | `FALL_THROUGH`
<a id="insn-00bb2b30"></a> `00bb2b30` | `3f b9 00 71` | cmp w9,#0x2e | `FALL_THROUGH`
<a id="insn-00bb2b34"></a> `00bb2b34` | `61 ff ff 54` | b.ne 0x00bb2b20 | `CONDITIONAL_JUMP`
<a id="insn-00bb2b38"></a> `00bb2b38` | `7f 04 00 b1` | cmn x3,#0x1 | `FALL_THROUGH`
<a id="insn-00bb2b3c"></a> `00bb2b3c` | `80 00 00 54` | b.eq 0x00bb2b4c | `CONDITIONAL_JUMP`
<a id="insn-00bb2b40"></a> `00bb2b40` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bb2b44"></a> `00bb2b44` | `e4 03 01 aa` | mov x4,x1 | `FALL_THROUGH`
<a id="insn-00bb2b48"></a> `00bb2b48` | `2a a2 02 14` | b 0x00c5b3f0 | `CALL_TERMINATOR`
<a id="insn-00bb2b4c"></a> `00bb2b4c` | `99 a1 02 14` | b 0x00c5b1b0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb2afc`](#insn-00bb2afc) 範囲 `[['00bb2afc', '00bb2b1f']]`
  - `CONDITIONAL_JUMP` [`00bb2b1c`](#insn-00bb2b1c) → [`00bb2b4c`](#insn-00bb2b4c)
  - `FALL_THROUGH` [`00bb2b1c`](#insn-00bb2b1c) → [`00bb2b20`](#insn-00bb2b20)
- ブロック [`00bb2b20`](#insn-00bb2b20) 範囲 `[['00bb2b20', '00bb2b23']]`
  - `CONDITIONAL_JUMP` [`00bb2b20`](#insn-00bb2b20) → [`00bb2b4c`](#insn-00bb2b4c)
  - `FALL_THROUGH` [`00bb2b20`](#insn-00bb2b20) → [`00bb2b24`](#insn-00bb2b24)
- ブロック [`00bb2b24`](#insn-00bb2b24) 範囲 `[['00bb2b24', '00bb2b37']]`
  - `CONDITIONAL_JUMP` [`00bb2b34`](#insn-00bb2b34) → [`00bb2b20`](#insn-00bb2b20)
  - `FALL_THROUGH` [`00bb2b34`](#insn-00bb2b34) → [`00bb2b38`](#insn-00bb2b38)
- ブロック [`00bb2b38`](#insn-00bb2b38) 範囲 `[['00bb2b38', '00bb2b3f']]`
  - `CONDITIONAL_JUMP` [`00bb2b3c`](#insn-00bb2b3c) → [`00bb2b4c`](#insn-00bb2b4c)
  - `FALL_THROUGH` [`00bb2b3c`](#insn-00bb2b3c) → [`00bb2b40`](#insn-00bb2b40)
- ブロック [`00bb2b40`](#insn-00bb2b40) 範囲 `[['00bb2b40', '00bb2b4b']]`
- ブロック [`00bb2b4c`](#insn-00bb2b4c) 範囲 `[['00bb2b4c', '00bb2b4f']]`

## 命令位置別の参照

- [`00bb2b1c`](#insn-00bb2b1c) → [`00bb2b4c`](#insn-00bb2b4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb2b20`](#insn-00bb2b20) → [`00bb2b4c`](#insn-00bb2b4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb2b34`](#insn-00bb2b34) → [`00bb2b20`](#insn-00bb2b20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb2b3c`](#insn-00bb2b3c) → [`00bb2b4c`](#insn-00bb2b4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb2b48`](#insn-00bb2b48) → [`00c5b3f0`](../00c5b/00c5b3f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b3f0` · 推定シンボル `None` · 推定型 `None`
- [`00bb2b4c`](#insn-00bb2b4c) → [`00c5b1b0`](../00c5b/00c5b1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b1b0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb2b1c`](#insn-00bb2b1c)

~~~json
{
  "source": "00bb2b1c",
  "target": "00bb2b4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb2b20`](#insn-00bb2b20)

~~~json
{
  "source": "00bb2b20",
  "target": "00bb2b4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb2b34`](#insn-00bb2b34)

~~~json
{
  "source": "00bb2b34",
  "target": "00bb2b20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb2b3c`](#insn-00bb2b3c)

~~~json
{
  "source": "00bb2b3c",
  "target": "00bb2b4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb2b48`](#insn-00bb2b48)

~~~json
{
  "source": "00bb2b48",
  "target": "00c5b3f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb2b4c`](#insn-00bb2b4c)

~~~json
{
  "source": "00bb2b4c",
  "target": "00c5b1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
