#include "kbcs_core.h"
#include <algorithm>

extern "C" uint32_t kbcs_core_motion_playback(const KbcsMotionPlaybackInput* in, KbcsMotionPlaybackOutput* out) {
    if (!in || !out || in->elapsed < 0 || in->elapsed > 1000000 || in->soul_frames < 0 || in->special_frames < 0 || in->soul_frames > 30000 || in->special_frames > 30000) return 1;
    // 通常体力KBは24F。移動はモデル姿勢とは別に加える。
    constexpr int jump[] = {0,-125,-125,-75,-75,-25,-25,0,0,25,25,75,75,125,125,-50,-50,-25,-25,25,25,50,50,0};
    KbcsMotionPlaybackOutput value{};
    const int age = std::min(in->elapsed, 23);
    value.x = age * 6.0;
    if (in->elapsed < 24) {
        value.frame = age;
        for (int index = 1; index <= age; ++index) value.y += jump[index] / 10.0;
    } else {
        value.frame = in->elapsed - 24;
        value.phase = value.frame < std::max({1, in->soul_frames, in->special_frames}) ? 1 : 2;
    }
    *out = value;
    return 0;
}
