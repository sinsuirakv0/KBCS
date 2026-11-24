# 00bf3cfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf2d08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2d08.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/machine_only_observed-0022.md#compare-fd452e2e0f61ab59f4fd1d200b05b3ca)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf3cfc",
  "name": "_ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEC1ERKS5_RKS4_",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "30b9515588040678ec18cb9f745b36ebddb7fd61982468964d6d4fc301e723e3",
  "source_text_sha256": "30b9515588040678ec18cb9f745b36ebddb7fd61982468964d6d4fc301e723e3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf3cfc",
        "00bf3d27"
      ]
    ],
    "bytes_sha256": "9b00a512578e4a012797bcbc3644bfc52e6922559bbe2dc52e5a8e21a820760d",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [006d7aec](../006d7/006d7aec.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 501 bytes

~~~c

void _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEC1ERKS5_RKS4_
               (undefined8 *param_1,byte *param_2)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if ((*param_2 & 1) == 0) {
    uVar2 = *(undefined8 *)(param_2 + 8);
    uVar1 = *(undefined8 *)param_2;
    param_1[2] = *(undefined8 *)(param_2 + 0x10);
    param_1[1] = uVar2;
    *param_1 = uVar1;
    return;
  }
  FUN_006d7aec(param_1,*(undefined8 *)(param_2 + 0x10),*(undefined8 *)(param_2 + 8));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf3cfc"></a> `00bf3cfc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bf3d00"></a> `00bf3d00` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00bf3d04"></a> `00bf3d04` | `c8 00 00 37` | tbnz w8,#0x0,0x00bf3d1c | `CONDITIONAL_JUMP`
<a id="insn-00bf3d08"></a> `00bf3d08` | `28 08 40 f9` | ldr x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bf3d0c"></a> `00bf3d0c` | `20 00 c0 3d` | ldr q0,[x1] | `FALL_THROUGH`
<a id="insn-00bf3d10"></a> `00bf3d10` | `08 08 00 f9` | str x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bf3d14"></a> `00bf3d14` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-00bf3d18"></a> `00bf3d18` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bf3d1c"></a> `00bf3d1c` | `22 a0 40 a9` | ldp x2,x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bf3d20"></a> `00bf3d20` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bf3d24"></a> `00bf3d24` | `72 8f eb 17` | b 0x006d7aec | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf3cfc`](#insn-00bf3cfc) 範囲 `[['00bf3cfc', '00bf3d07']]`
  - `CONDITIONAL_JUMP` [`00bf3d04`](#insn-00bf3d04) → [`00bf3d1c`](#insn-00bf3d1c)
  - `FALL_THROUGH` [`00bf3d04`](#insn-00bf3d04) → [`00bf3d08`](#insn-00bf3d08)
- ブロック [`00bf3d08`](#insn-00bf3d08) 範囲 `[['00bf3d08', '00bf3d1b']]`
- ブロック [`00bf3d1c`](#insn-00bf3d1c) 範囲 `[['00bf3d1c', '00bf3d27']]`

## 命令位置別の参照

- [`00bf3d04`](#insn-00bf3d04) → [`00bf3d1c`](#insn-00bf3d1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3d24`](#insn-00bf3d24) → [`006d7aec`](../006d7/006d7aec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006d7aec` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf3d04`](#insn-00bf3d04)

~~~json
{
  "source": "00bf3d04",
  "target": "00bf3d1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3d24`](#insn-00bf3d24)

~~~json
{
  "source": "00bf3d24",
  "target": "006d7aec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
