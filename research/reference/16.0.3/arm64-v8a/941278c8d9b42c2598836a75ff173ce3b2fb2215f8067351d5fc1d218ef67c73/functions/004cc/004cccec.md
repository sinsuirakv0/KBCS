# 004cccec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `004cc9cc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc9cc.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/machine_only_observed-0002.md#compare-7acbded2aa70cbe81d582b01a3a6788a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004cccec",
  "name": "_ZN5Botan10hex_decodeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "75107ca700aab970a10909437c44114c49ab45289eaeca65a478c736c759cd3e",
  "source_text_sha256": "75107ca700aab970a10909437c44114c49ab45289eaeca65a478c736c759cd3e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004cccec",
        "004ccd0b"
      ]
    ],
    "bytes_sha256": "f7ca8fb4aa022c36344842bfced9500553ff9bd9ad8809009281320ab6a2787c",
    "instruction_count": 8,
    "instruction_bytes": 32,
    "body_bytes": 32,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5a200](../00c5a/00c5a200.md)

## 呼び出し先

- [00c5a1f0](../00c5a/00c5a1f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 421 bytes

~~~c

void _ZN5Botan10hex_decodeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb
               (byte *param_1,undefined4 param_2)

{
  ulong uVar1;
  byte *pbVar2;
  
  uVar1 = *(ulong *)(param_1 + 8);
  pbVar2 = *(byte **)(param_1 + 0x10);
  if ((*param_1 & 1) == 0) {
    pbVar2 = param_1 + 1;
    uVar1 = (ulong)(*param_1 >> 1);
  }
  _ZN5Botan10hex_decodeEPKcmb(pbVar2,uVar1,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004cccec"></a> `004cccec` | `09 00 40 39` | ldrb w9,[x0] | `FALL_THROUGH`
<a id="insn-004cccf0"></a> `004cccf0` | `0b a8 40 a9` | ldp x11,x10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-004cccf4"></a> `004cccf4` | `e2 03 01 2a` | mov w2,w1 | `FALL_THROUGH`
<a id="insn-004cccf8"></a> `004cccf8` | `2c fd 41 d3` | lsr x12,x9,#0x1 | `FALL_THROUGH`
<a id="insn-004cccfc"></a> `004cccfc` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-004ccd00"></a> `004ccd00` | `40 15 80 9a` | csinc x0,x10,x0,ne | `FALL_THROUGH`
<a id="insn-004ccd04"></a> `004ccd04` | `81 01 8b 9a` | csel x1,x12,x11,eq | `FALL_THROUGH`
<a id="insn-004ccd08"></a> `004ccd08` | `3a 35 1e 14` | b 0x00c5a1f0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004cccec`](#insn-004cccec) 範囲 `[['004cccec', '004ccd0b']]`

## 命令位置別の参照

- [`004ccd08`](#insn-004ccd08) → [`00c5a1f0`](../00c5a/00c5a1f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a1f0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004ccd08`](#insn-004ccd08)

~~~json
{
  "source": "004ccd08",
  "target": "00c5a1f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
