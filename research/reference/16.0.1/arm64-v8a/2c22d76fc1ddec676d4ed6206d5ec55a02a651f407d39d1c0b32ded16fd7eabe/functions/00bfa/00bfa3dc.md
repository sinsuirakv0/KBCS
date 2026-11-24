# 00bfa3dc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bf9fb4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9fb4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0040.md#compare-44953720bce21203ce0fe5763186c76b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfa478`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa478.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-9e0af1983df2d00984fad1b4f06122e6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfa3dc",
  "name": "_ZNSt6__ndk111timed_mutex8try_lockEv",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "41d5e36ba8584ba38fd4f465786283fa3349aa905ab9390120ff767dab81c772",
  "source_text_sha256": "41d5e36ba8584ba38fd4f465786283fa3349aa905ab9390120ff767dab81c772",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfa3dc",
        "00bfa433"
      ]
    ],
    "bytes_sha256": "eed98a9e66c72a9a8833425d036ba07da5eab24dc76c27e7d2411b90dc53d022",
    "instruction_count": 22,
    "instruction_bytes": 88,
    "body_bytes": 88,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b6b0](../00c5b/00c5b6b0.md)
- [00c5e270](../00c5e/00c5e270.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 413 bytes

~~~c

bool _ZNSt6__ndk111timed_mutex8try_lockEv(pthread_mutex_t *param_1)

{
  bool bVar1;
  int iVar2;
  
  iVar2 = pthread_mutex_trylock(param_1);
  if (iVar2 == 0) {
    bVar1 = *(byte *)((long)param_1 + 0x58) == 0;
    if ((*(byte *)((long)param_1 + 0x58) & 1) == 0) {
      *(undefined1 *)((long)param_1 + 0x58) = 1;
    }
    pthread_mutex_unlock(param_1);
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfa3dc"></a> `00bfa3dc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfa3e0"></a> `00bfa3e0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfa3e4"></a> `00bfa3e4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfa3e8"></a> `00bfa3e8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfa3ec"></a> `00bfa3ec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfa3f0"></a> `00bfa3f0` | `a0 8f 01 94` | bl 0x00c5e270 | `UNCONDITIONAL_CALL`
<a id="insn-00bfa3f4"></a> `00bfa3f4` | `60 00 00 34` | cbz w0,0x00bfa400 | `CONDITIONAL_JUMP`
<a id="insn-00bfa3f8"></a> `00bfa3f8` | `f4 03 1f 2a` | mov w20,wzr | `FALL_THROUGH`
<a id="insn-00bfa3fc"></a> `00bfa3fc` | `09 00 00 14` | b 0x00bfa420 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfa400"></a> `00bfa400` | `68 62 41 39` | ldrb w8,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bfa404"></a> `00bfa404` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00bfa408"></a> `00bfa408` | `f4 17 9f 1a` | cset w20,eq | `FALL_THROUGH`
<a id="insn-00bfa40c"></a> `00bfa40c` | `68 00 00 37` | tbnz w8,#0x0,0x00bfa418 | `CONDITIONAL_JUMP`
<a id="insn-00bfa410"></a> `00bfa410` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfa414"></a> `00bfa414` | `68 62 01 39` | strb w8,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bfa418"></a> `00bfa418` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfa41c"></a> `00bfa41c` | `a5 84 01 94` | bl 0x00c5b6b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfa420"></a> `00bfa420` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00bfa424"></a> `00bfa424` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfa428"></a> `00bfa428` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfa42c"></a> `00bfa42c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfa430"></a> `00bfa430` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfa3dc`](#insn-00bfa3dc) 範囲 `[['00bfa3dc', '00bfa3f7']]`
  - `CONDITIONAL_JUMP` [`00bfa3f4`](#insn-00bfa3f4) → [`00bfa400`](#insn-00bfa400)
  - `FALL_THROUGH` [`00bfa3f4`](#insn-00bfa3f4) → [`00bfa3f8`](#insn-00bfa3f8)
- ブロック [`00bfa3f8`](#insn-00bfa3f8) 範囲 `[['00bfa3f8', '00bfa3ff']]`
  - `UNCONDITIONAL_JUMP` [`00bfa3fc`](#insn-00bfa3fc) → [`00bfa420`](#insn-00bfa420)
- ブロック [`00bfa400`](#insn-00bfa400) 範囲 `[['00bfa400', '00bfa40f']]`
  - `CONDITIONAL_JUMP` [`00bfa40c`](#insn-00bfa40c) → [`00bfa418`](#insn-00bfa418)
  - `FALL_THROUGH` [`00bfa40c`](#insn-00bfa40c) → [`00bfa410`](#insn-00bfa410)
- ブロック [`00bfa410`](#insn-00bfa410) 範囲 `[['00bfa410', '00bfa417']]`
  - `FALL_THROUGH` [`00bfa414`](#insn-00bfa414) → [`00bfa418`](#insn-00bfa418)
- ブロック [`00bfa418`](#insn-00bfa418) 範囲 `[['00bfa418', '00bfa41f']]`
  - `FALL_THROUGH` [`00bfa41c`](#insn-00bfa41c) → [`00bfa420`](#insn-00bfa420)
- ブロック [`00bfa420`](#insn-00bfa420) 範囲 `[['00bfa420', '00bfa433']]`

## 命令位置別の参照

- [`00bfa3e0`](#insn-00bfa3e0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa3e4`](#insn-00bfa3e4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa3f0`](#insn-00bfa3f0) → [`00c5e270`](../00c5e/00c5e270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e270` · 推定シンボル `None` · 推定型 `None`
- [`00bfa3f4`](#insn-00bfa3f4) → [`00bfa400`](#insn-00bfa400) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa3fc`](#insn-00bfa3fc) → [`00bfa420`](#insn-00bfa420) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa40c`](#insn-00bfa40c) → [`00bfa418`](#insn-00bfa418) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa41c`](#insn-00bfa41c) → [`00c5b6b0`](../00c5b/00c5b6b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b6b0` · 推定シンボル `None` · 推定型 `None`
- [`00bfa424`](#insn-00bfa424) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa428`](#insn-00bfa428) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfa3e0`](#insn-00bfa3e0)

~~~json
{
  "source": "00bfa3e0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa3e4`](#insn-00bfa3e4)

~~~json
{
  "source": "00bfa3e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa3f0`](#insn-00bfa3f0)

~~~json
{
  "source": "00bfa3f0",
  "target": "00c5e270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa3f4`](#insn-00bfa3f4)

~~~json
{
  "source": "00bfa3f4",
  "target": "00bfa400",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa3fc`](#insn-00bfa3fc)

~~~json
{
  "source": "00bfa3fc",
  "target": "00bfa420",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa40c`](#insn-00bfa40c)

~~~json
{
  "source": "00bfa40c",
  "target": "00bfa418",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa41c`](#insn-00bfa41c)

~~~json
{
  "source": "00bfa41c",
  "target": "00c5b6b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa424`](#insn-00bfa424)

~~~json
{
  "source": "00bfa424",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa428`](#insn-00bfa428)

~~~json
{
  "source": "00bfa428",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
